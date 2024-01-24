Task name => Bash

Task preparation =>  First we make a folder named Bash where we will put all the needed files inside.

Task implementation => what is the way you have implemented this? (bash script)

You create a python script named restconf_put_get_interface.py
inside you will put the following code.

# import requests
# requests.packages.urllib3.disable_warnings()

# IP_HOST = "192.168.56.107"
# RESTCONF_USERNAME="cisco"
# RESTCONF_PASSWORD="cisco123!"
# DATA_FORMAT="application/yang-data+json"
# LOOPBACK_INTERFACE="Loopback199"
# LOOPBACK_IP="10.1.99.1"

# api_url_put = f"https://{IP_HOST}/restconf/data/ietf-interfaces:interfaces/interface={LOOPBACK_INTERFACE}"
# api_url_get = f"https://{IP_HOST}/restconf/data/ietf-interfaces:interfaces"
# headers = { "Accept": DATA_FORMAT ,  "Content-type": DATA_FORMAT }
# basicauth = (RESTCONF_USERNAME, RESTCONF_PASSWORD)
# yangConfig = {
#  "ietf-interfaces:interface": {
 #    "name": LOOPBACK_INTERFACE,
#     "description": f"RESTCONF => {LOOPBACK_INTERFACE}",
#     "type": "iana-if-type:softwareLoopback",
#     "enabled": True,
#     "ietf-ip:ipv4": {
  #       "address": [
    #         {
      #           "ip": LOOPBACK_IP,
       #          "netmask": "255.255.255.0"
        #     }
#          ]
   #  }
 # }
# }

# resp_put = requests.put(api_url_put, json=yangConfig, auth=basicauth, headers=headers, verify=False)

# if resp_put.status_code in range(200,300):
 #   print(f"STATUS OK: {resp_put.status_code}") 
# else:
#    print("ERROR") 
#    print(resp_put.status_code)
 #   print(resp_put.text)

# resp_get = requests.get(api_url_get, auth=basicauth, headers=headers, verify=False)
# print(resp_get.text)

After you will need to create a bash file named restconf_api.sh with the following code

# #!/bin/bash

# RESTCONF API endpoints
# IP_HOST="192.168.56.107"
# RESTCONF_USERNAME="cisco"
# RESTCONF_PASSWORD="cisco123!"
# DATA_FORMAT="application/yang-data+json"
# LOOPBACK_INTERFACE="Loopback199"
# LOOPBACK_IP="10.1.99.1"

# api_url_put="https://${IP_HOST}/restconf/data/ietf-interfaces:interfaces/interface=${LOOPBACK_INTERFACE}"
# api_url_get="https://${IP_HOST}/restconf/data/ietf-interfaces:interfaces"
# headers="-H 'Accept: ${DATA_FORMAT}' -H 'Content-type: ${DATA_FORMAT}'"
# basicauth="-u ${RESTCONF_USERNAME}:${RESTCONF_PASSWORD}"
# yangConfig='{
 # "ietf-interfaces:interface": {
    # "name": "'${LOOPBACK_INTERFACE}'",
    # "description": "RESTCONF => '${LOOPBACK_INTERFACE}'",
    # "type": "iana-if-type:softwareLoopback",
    # "enabled": true,
    # "ietf-ip:ipv4": {
       #  "address": [
      #       {
     #            "ip": "'${LOOPBACK_IP}'",
    #             "netmask": "255.255.255.0"
   #          }
  #       ]
 #    }
# }
# }'

# Output to check_restconf_api.txt
# {
   # # First line: today's date
   # echo "Today's date: $(date)"

   # # Next line: START REST API CALL
   # echo "START REST API CALL"
   # echo "============"

   # # First API Call
   # echo "FIRST API CALL"
   # echo "============"
    
   # # Debug: Print details about the request
   # echo "Curl PUT Command:"
   # echo "curl -i -X PUT $api_url_put -d \"$yangConfig\" $basicauth $headers --insecure"
    
   # # Perform the RESTCONF PUT request
   # resp_put=$(curl -i -X PUT $api_url_put -d "$yangConfig" $basicauth $headers --insecure)

   # # Extract and Output Status Code
   # status_code_put=$(echo "$resp_put" | grep HTTP/ | awk '{print $2}')
   # echo "Status Code (PUT): $status_code_put"
   # echo "============"

   # # Second API Call
   # echo "SECOND API CALL"
   # echo "============"
    
   # # Debug: Print details about the request
   # echo "Curl GET Command:"
   # echo "curl -i -X GET $api_url_get $basicauth $headers --insecure"
    
   # # Perform the RESTCONF GET request
   # resp_get=$(curl -i -X GET $api_url_get $basicauth $headers --insecure)

   # # Extract and Output Status Code
   # status_code_get=$(echo "$resp_get" | grep HTTP/ | awk '{print $2}')
   # echo "Status Code (GET): $status_code_get"
    
   # # Extract and Output Specific Field (e.g., interface names)
   # interfaces=$(echo "$resp_get" | jq -r '.data | .["ietf-interfaces:interfaces"] | .interface | .[].name')
   # echo "Interfaces: $interfaces"

   # echo "============"

  #  # Last line: END REST API CALL
 #   echo "END REST API CALL"
# } >| check_restconf_api.txt

This bash file speaks with the server via json filer to get information, 
at the end of the script it will create a txt file with the answer init

terminal:
  python3 restconf_put_get_interface.py
  nano restconf_api.sh
  chmod +x restconf_api.sh
  ./restconf_api.sh

Task troubleshooting => what were the problems encountered? Error ocurred with 443 code while the port is open.

Task verification => proof of the quality of the resultt.
https://github.com/DannyRodriguezRincon/Devasc-Skills_DannyRodriguez/blob/7d9a3d9c4ccda34ece58a8de0486eeae054fa247/Bash/Bash-answerfile.png
