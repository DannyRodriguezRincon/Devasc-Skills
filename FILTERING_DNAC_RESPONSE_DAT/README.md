Task name => DNAC FILTERING

Task preparation => what preparation is necessary to perform the task?
  First we make a folder named FILTERING_DNAC_RESPONSE_DAT where we will put all the needed files inside.
  Then we copy the DNAC SAMPLE script into the Bash folder
  
# import XXXXAXXXX
# import datetime
# import json
# requests.packages.XXXXBXXXX.disable_warnings()

# DNAC_scheme = 'https://'
# DNAC_authority='sandboxdnac.cisco.com'
# DNAC_port=':443'
# DNAC_path_token='/dna/system/api/v1/auth/token'
# DNAC_path='/dna/intent/api/v1/network-device'
# DNAC_user = 'devnetuser'
# DNAC_psw = 'Cisco123!'

# # DATE AND TIME
# print ("Current date and time: ")
# print(datetime.XXXXCXXXX)

# # TOKEN REQUEST
# token_req_url = DNAC_scheme+DNAC_authority+DNAC_path_token
# auth = (DNAC_user, DNAC_psw)
# req = requests.request('XXXXDXXXX', token_req_url, auth=auth, verify=False)
# token = req.json()['Token']

# # INVENTORY REQUEST
# req_url = DNAC_scheme+DNAC_authority+DNAC_port+DNAC_path
# headers = {'X-AUTH-TOKEN': XXXXEXXXX}
# resp_devices = requests.request('GET', req_url, headers=XXXXFXXXX, verify=False)
# resp_devices_json = resp_devices.json()

# # FILTER RESPONSE DATA
# for device in resp_devices_json['response']:
 #   if device['type'] != None:
  #      print('===')
   #     print('Hostname: ' + device['hostname'])
    #    print('Family  : ' + device[''XXXXGXXXX'])
     #   print('MAC: '+ device['XXXXHXXXX'])
      #  print('IP: ' + device['XXXXIXXXX'])
      #  print('Software version: ' + device['softwareVersion'])
      #  print('Reachability: ' + device['XXXXJXXXX'])

Task implementation => what is the way you have implemented this?
  After founding the right missing parts the final code is this
  
# import requests
# import datetime
# import json
# requests.packages.urllib3.disable_warnings()

# DNAC_scheme = 'https://'
# DNAC_authority='sandboxdnac.cisco.com'
# DNAC_port=':443'
# DNAC_path_token='/dna/system/api/v1/auth/token'
# DNAC_path='/dna/intent/api/v1/network-device'
# DNAC_user = 'devnetuser'
# DNAC_psw = 'Cisco123!'

# # DATE AND TIME
# print("Current date and time: ")
# print(datetime.datetime.now())

# # TOKEN REQUEST
# token_req_url = DNAC_scheme + DNAC_authority + DNAC_path_token
# auth = (DNAC_user, DNAC_psw)
#req = requests.request('POST', token_req_url, auth=auth, verify=False)
# token = req.json()['Token']

# # INVENTORY REQUEST
# req_url = DNAC_scheme + DNAC_authority + DNAC_port + DNAC_path
# headers = {'X-Auth-Token': token}
# resp_devices = requests.request('GET', req_url, headers=headers, verify=False)
# resp_devices_json = resp_devices.json()

# # FILTER RESPONSE DATA
# for device in resp_devices_json['response']:
 #    if device['type'] is not None:
   #     print('===')
    #    print('Hostname: ' + device['hostname'])
     #   print('Family  : ' + device['family'])
      #  print('MAC: ' + device['macAddress'])
       # print('IP: ' + device['managementIpAddress'])
       # print('Software version: ' + device['softwareVersion'])
       # print('Reachability: ' + device['reachabilityStatus'])

Task troubleshooting => what were the problems encountered? No problem occured.

Task verification => proof of the quality of the result
https://github.com/DannyRodriguezRincon/Devasc-Skills_DannyRodriguez/blob/4c0a3623124032eaece9bfcfd230e44a5098bd5b/FILTERING_DNAC_RESPONSE_DAT/DNAC_Filtering_answer.png
