const request = require('supertest');
const { spawn } = require('child_process');

const PORT = process.env.FRONTEND_PORT || process.env.PORT || 3000;
const BASE = `http://127.0.0.1:${PORT}`;
let serverProcess;
let agent;

// Poll the server until /config.js is reachable or timeout
beforeAll(async () => {
  // start the frontend server using the Python script
  serverProcess = spawn('python', ['frontend_server.py'], {
    env: { ...process.env, FRONTEND_PORT: PORT },
    stdio: 'inherit'
  });

  agent = request(BASE);
  const start = Date.now();
  const timeoutMs = 10000; // 10 seconds
  const interval = 300;

  while (true) {
    try {
      const res = await agent.get('/config.js');
      if (res.status === 200) {
        break;
      }
    } catch (err) {
      // ignore connection errors during startup
    }
    if (Date.now() - start > timeoutMs) {
      throw new Error(`Frontend server not reachable at ${BASE} within 10 seconds`);
    }
    await new Promise((resolve) => setTimeout(resolve, interval));
  }
}, 15000);

afterAll(() => {
  if (serverProcess) {
    serverProcess.kill();
  }
});

test('config.js responds with javascript', async () => {
  const res = await agent.get('/config.js');
  expect(res.status).toBe(200);
  expect(res.text).toMatch(/BACKEND_API_URL/);
});

