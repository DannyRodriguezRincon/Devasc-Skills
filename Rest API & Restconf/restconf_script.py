import requests
from requests.auth import HTTPBasicAuth

# Replace with your credentials or use the provided sandbox credentials
username = 'Danny Rodriguez'
password = 'knaller'

# Example 1: Get Device Information
url1 = 'https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native'
response1 = requests.get(url1, auth=HTTPBasicAuth(username, password), verify=False)

print("Example 1 - Get Device Information:")
print(response1.json())

# Example 2: Get Interface Information
url2 = 'https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces'
response2 = requests.get(url2, auth=HTTPBasicAuth(username, password), verify=False)

print("Example 2 - Get Interface Information:")
print(response2.json())

# Example 3: Create a fictional resource (Modify Device Configuration)
url3 = 'https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces/interface=Loopback99'
headers = {'Content-Type': 'application/yang-data+json'}
payload = '{"ietf-interfaces:interface": {"name": "Loopback99", "type": "iana-if-type:softwareLoopback"}}'
response3 = requests.put(url3, auth=HTTPBasicAuth(username, password), headers=headers, data=payload, verify=False)

print("Example 3 - Create a fictional resource (Modify Device Configuration):")
print(response3.status_code)
