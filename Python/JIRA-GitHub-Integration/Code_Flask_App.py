from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth
import json
import os

app = Flask(__name__)  # Creating a flask app instance


# Endpoint to create JIRA ticket
@app.route("/createJIRA", methods=['POST'])  # Fixed typo here
def createJIRA():
    url = "https://testingbyme0011.atlassian.net/rest/api/3/issue"

    # Getting the API token and email from environment variables for better security
    API_TOKEN = os.getenv("JIRA_API_TOKEN")  # Set this as an environment variable
    EMAIL = os.getenv("JIRA_EMAIL")  # Set this as an environment variable

    if not API_TOKEN or not EMAIL:
        return jsonify({"error": "API token or email not found in environment variables"}), 400

    API_TOKEN = "ATATT********BC"

    auth = HTTPBasicAuth("testingbyme0011@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # The payload for creating a JIRA issue
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
        return jsonify(json.loads(response.text)), 201
    else:
        print(f"Failed to create JIRA issue. Status code: {response.status_code}")
        print("Response content:", response.text)
        return jsonify({"error": "Failed to create issue", "status_code": response.status_code,
                        "response": response.text}), response.status_code


# Running the Flask app
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
