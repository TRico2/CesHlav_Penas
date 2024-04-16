"""Constants for the AZ router integration."""

from datetime import timedelta

DOMAIN = "azrouter"

ATTRIBUTION = "Data provided by AZ router"
MANUFACTURER = "AZTraders"
SCAN_INTERVAL = timedelta(seconds=10)

AZ_GET_HEADERS = {
            'authorization': 'eyJhY2Nlc3MiOiJzZXJ2aWNlIn0',
            'Accept': 'application/json, text/plain, */*',
            'Cookie': 'token=eyJhY2Nlc3MiOiJzZXJ2aWNlIn0',
           }

AZ_POST_HEADERS = {'authorization': 'eyJhY2Nlc3MiOiJzZXJ2aWNlIn0',
           'Accept': 'application/json, text/plain, */*',
           'Cookie': 'token=eyJhY2Nlc3MiOiJzZXJ2aWNlIn0',
           'Content-Type': 'application/json',
           }