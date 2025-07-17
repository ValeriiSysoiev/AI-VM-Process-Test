param location string
param environmentName string
param orchestratorName string
param ingestionName string
param frontendAppName string
param triageName string
param remediationName string
param reportingName string
param orchestratorImage string = 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
param ingestionImage string = 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
param frontendImage string = 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
param triageImage string = 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
param remediationImage string = 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
param reportingImage string = 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
param minReplicas int = 1
param maxReplicas int = 1
param cpu string = '0.5'
param memory string = '1Gi'
param registryLoginServer string
param registryUsername string
param registryPassword string

resource env 'Microsoft.App/managedEnvironments@2023-05-01' = {
  name: environmentName
  location: location
  properties: {}
}

resource orchestrator 'Microsoft.App/containerApps@2023-05-01' = {
  name: orchestratorName
  location: location
  tags: {
    'azd-service-name': 'orchestrator'
  }
  properties: {
    environmentId: env.id
    configuration: {
      registries: [
        {
          server: registryLoginServer
          username: registryUsername
          passwordSecretRef: 'acr-pwd'
        }
      ]
      secrets: [
        {
          name: 'acr-pwd'
          value: registryPassword
        }
      ]
    }
    template: {
      containers: [
        {
          name: orchestratorName
          image: orchestratorImage
          resources: {
            cpu: json(cpu)
            memory: memory
          }
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
      }
    }
  }
}

resource ingestion 'Microsoft.App/containerApps@2023-05-01' = {
  name: ingestionName
  location: location
  tags: {
    'azd-service-name': 'ingestion_agents'
  }
  properties: {
    environmentId: env.id
    configuration: {
      registries: [
        {
          server: registryLoginServer
          username: registryUsername
          passwordSecretRef: 'acr-pwd'
        }
      ]
      secrets: [
        {
          name: 'acr-pwd'
          value: registryPassword
        }
      ]
    }
    template: {
      containers: [
        {
          name: ingestionName
          image: ingestionImage
          resources: {
            cpu: json(cpu)
            memory: memory
          }
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
      }
    }
  }
}

resource frontend 'Microsoft.App/containerApps@2023-05-01' = {
  name: frontendAppName
  location: location
  tags: {
    'azd-service-name': 'frontend'
  }
  properties: {
    environmentId: env.id
    configuration: {
      registries: [
        {
          server: registryLoginServer
          username: registryUsername
          passwordSecretRef: 'acr-pwd'
        }
      ]
      secrets: [
        {
          name: 'acr-pwd'
          value: registryPassword
        }
      ]
    }
    template: {
      containers: [
        {
          name: frontendAppName
          image: frontendImage
          resources: {
            cpu: json(cpu)
            memory: memory
          }
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
      }
    }
  }
}

resource triage 'Microsoft.App/containerApps@2023-05-01' = {
  name: triageName
  location: location
  tags: {
    'azd-service-name': 'triage_agents'
  }
  properties: {
    environmentId: env.id
    configuration: {
      registries: [
        {
          server: registryLoginServer
          username: registryUsername
          passwordSecretRef: 'acr-pwd'
        }
      ]
      secrets: [
        {
          name: 'acr-pwd'
          value: registryPassword
        }
      ]
    }
    template: {
      containers: [
        {
          name: triageName
          image: triageImage
          resources: {
            cpu: json(cpu)
            memory: memory
          }
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
      }
    }
  }
}

resource remediation 'Microsoft.App/containerApps@2023-05-01' = {
  name: remediationName
  location: location
  tags: {
    'azd-service-name': 'remediation_agents'
  }
  properties: {
    environmentId: env.id
    configuration: {
      registries: [
        {
          server: registryLoginServer
          username: registryUsername
          passwordSecretRef: 'acr-pwd'
        }
      ]
      secrets: [
        {
          name: 'acr-pwd'
          value: registryPassword
        }
      ]
    }
    template: {
      containers: [
        {
          name: remediationName
          image: remediationImage
          resources: {
            cpu: json(cpu)
            memory: memory
          }
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
      }
    }
  }
}

resource reporting 'Microsoft.App/containerApps@2023-05-01' = {
  name: reportingName
  location: location
  tags: {
    'azd-service-name': 'reporting_agents'
  }
  properties: {
    environmentId: env.id
    configuration: {
      registries: [
        {
          server: registryLoginServer
          username: registryUsername
          passwordSecretRef: 'acr-pwd'
        }
      ]
      secrets: [
        {
          name: 'acr-pwd'
          value: registryPassword
        }
      ]
    }
    template: {
      containers: [
        {
          name: reportingName
          image: reportingImage
          resources: {
            cpu: json(cpu)
            memory: memory
          }
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
      }
    }
  }
}
