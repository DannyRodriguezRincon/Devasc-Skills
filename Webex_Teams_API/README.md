Task 6 -- Webex Teams API 
Create or adapt an existing Python script to create a Webex Teams space with the name “devasc_skills_your_initials” with yourself and <yvan.rooseleer@biasc.be> as the members
<!-- import requests
import json

# Webex Teams API base URL
api_url = "https://api.ciscospark.com/v1"

# Your Webex Teams API token
api_token = "MTYxYjM2ZDUtYzYyNC00NGI5LTllMjQtMTlkYjEyNzQ2ZTYxNmM3MWUyN2YtOGQ1_PE93_6b68d305-fbad-4d67-8d3d-6414c9902447"

# Members' email addresses
your_email = "danny.rodriguezrincon@student.odisee.be"
yvan_email = "yvan.rooseleer@biasc.be"

# Webex Teams space name
space_name = "devasc_skills_DannyRodriguez"

# Function to create a Webex teams
def create_space(api_url, api_token, space_name):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }
    payload = {"title": space_name}
    response = requests.post(f"{api_url}/rooms", headers=headers, json=payload)
    return response.json()["id"]

# Function to invite members to a Webex Teams space
def invite_members(api_url, api_token, space_id, email_list):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }
    for email in email_list:
        payload = {"roomId": space_id, "personEmail": email}
        requests.post(f"{api_url}/memberships", headers=headers, json=payload)

# message to webex teams
def send_message(api_url, api_token, space_id, message):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }
    payload = {"roomId": space_id, "text": message}
    requests.post(f"{api_url}/messages", headers=headers, json=payload)

# Create Webex team
space_id = create_space(api_url, api_token, space_name)

# Invite members to the group
invite_members(api_url, api_token, space_id, [your_email, yvan_email]) -->

Publish the url of your github remote repository (task 1 of the skills exam) in this new Webex Teams space

<!-- # Publish GitHub repository URL in the space
github_repo_url = "https://github.com/DannyRodriguezRincon/Devasc-Skills_DannyRodriguez.git"
send_message(api_url, api_token, space_id, f"Check out my GitHub repository: {github_repo_url}") -->

Create (or adapt) an existing Python script that sends a message “Here are my screenshots of devasc skills-based exam” to the new space
<!-- # Send a message to the space
send_message(api_url, api_token, space_id, "Here are my screenshots of devasc skills-based exam") -->


Upload one screenshot of every task to the Webex Teams Space

terminal: 
python3 scripts.py