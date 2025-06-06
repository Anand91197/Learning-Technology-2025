 # http://docs.python-requests.org
#https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/

import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://testingbyme0011.atlassian.net/rest/api/3/project"

API_TOKEN = "*******KOg6Sw4pRxwjtaxhH_jmW8LkL-btuwwN7_HKRN2vvbLbQ=9A6376BC"

auth = HTTPBasicAuth("testingbyme0011@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

output = json.loads(response.text)
name = output[0]["name"]
print(name)
