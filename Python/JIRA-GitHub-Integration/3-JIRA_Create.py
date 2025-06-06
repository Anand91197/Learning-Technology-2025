# This code sample uses the 'requests' library:
# http://docs.python-requests.org
#https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post


import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://testingbyme0011.atlassian.net/rest/api/3/issue"

API_TOKEN = "*********cbIn2Vx0WUjV1iL156_KOg6Sw4pRxwjtaxhH_jmW8LkL-btuwwN7_HKRN2vvbLbQ=9A6376BC"

auth = HTTPBasicAuth("testingbyme0011@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}
payload = json.dumps({
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My First JIRA Ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10002"  # Ensure this issue type ID exists in your Jira
    },
    "labels": [
      "bugfix"
    ],
    "project": {
      "key": "DEVOPS"  # Ensure this project key exists in your Jira
    },
    "summary": "Please automate the JIRA workflow"
  }
})

# Sending the POST request to Jira API
response = requests.post(
    url,
    data=payload,
    headers=headers,
    auth=auth
)


# Checking if the request was successful
if response.status_code == 201:
    print("JIRA issue created successfully!")
else:
    print(f"Failed to create JIRA issue. Status code: {response.status_code}")
    print("Response content:", response.text)

# Print the response in a readable format
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
