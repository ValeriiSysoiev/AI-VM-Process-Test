import json
import logging

import anyio

from src.agents.ingestion.ingestion_agent import fetch_nexpose_assets

logging.basicConfig(level=logging.INFO)


def main() -> None:
    """Run a quick connectivity check against the Nexpose API."""
    data = anyio.run(fetch_nexpose_assets)
    if data is None:
        print(
            "Failed to retrieve data from Nexpose. Check credentials and connectivity."
        )
    else:
        asset_count = len(data.get("resources", []))
        print(f"Successfully retrieved {asset_count} assets from Nexpose")
        print(json.dumps(data, indent=2)[:200])


if __name__ == "__main__":
    main()
