Task name => Rest API & Restconf

Task preparation => what preparation is necessary to perform the task?
 First we make a folder named Rest API & Restconf where we will put all the needed files inside.
 
Task implementation => what is the way you have implemented this? (python code)

# import requests
# from requests.auth import HTTPBasicAuth

# # Replace with your credentials or use the provided sandbox credentials
# username = 'Danny Rodriguez'
# password = 'knaller'

# # Example 1: Get Device Information
# url1 = 'https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native'
# response1 = requests.get(url1, auth=HTTPBasicAuth(username, password), verify=False)

# print("Example 1 - Get Device Information:")
# print(response1.json())

# # Example 2: Get Interface Information
# url2 = 'https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces'
# response2 = requests.get(url2, auth=HTTPBasicAuth(username, password), verify=False)

# print("Example 2 - Get Interface Information:")
# print(response2.json())

# # Example 3: Create a fictional resource (Modify Device Configuration)
# url3 = 'https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces/interface=Loopback99'
# headers = {'Content-Type': 'application/yang-data+json'}
# payload = '{"ietf-interfaces:interface": {"name": "Loopback99", "type": "iana-if-type:softwareLoopback"}}'
# response3 = requests.put(url3, auth=HTTPBasicAuth(username, password), headers=headers, data=payload, verify=False)

# print("Example 3 - Create a fictional resource (Modify Device Configuration):")
# print(response3.status_code)
# Task troubleshooting => what were the problems encountered?

# Task verification => proof of the quality of the result

Task troubleshooting => what were the problems encountered? Yes Error occured. see screenshots
https://github.com/DannyRodriguezRincon/Devasc-Skills_DannyRodriguez/blob/f9f4a0653420b3dc984ff15f05f2e2f4ac9b3296/Rest%20API%20%26%20Restconf/RestConf_Error.png

Task verification => proof of the quality of the result 
https://github.com/DannyRodriguezRincon/Devasc-Skills_DannyRodriguez/blob/d900d2b0e202749010c2e37e537d5d8baf12127b/Rest%20API%20%26%20Restconf/Restconf_Script_Answer.png


