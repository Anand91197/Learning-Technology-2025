# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createjira', methods=['POST'])
def createjira():

    url = "https://testingbyme0011.atlassian.net/rest/api/3/issue"

    API_TOKEN="**************llWzaIYGshPPso_ZbDICYMWYrcbIn2Vx0WUjV1iL156_KOg6Sw4pRxwjtaxhH_jmW8LkL-btuwwN7_HKRN2vvbLbQ=9A6376BC"

    auth = HTTPBasicAuth("testingbyme0011@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "To fix a Splunk Config",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "DEVOPS"
        },
        "issuetype": {
            "id": "10002"
        },
        "summary": "Please automate the Splunk config"
    },
    "update": {}
    } )


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    # Checking if the request was successful
    if response.status_code == 201:
        print("JIRA issue created successfully!")
        return jsonify(json.loads(response.text)), 201
    else:
        print(f"Failed to create JIRA issue. Status code: {response.status_code}")
        print("Response content:", response.text)
        return jsonify({"error": "Failed to create issue", "status_code": response.status_code,
                        "response": response.text}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
