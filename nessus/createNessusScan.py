#!/usr/bin/env python2.7
import requests, json

############################################################################
# SETTINGS
############################################################################
policy_template_id="policy_template_id => use the script getPolicies.py "
policy_id="policy_id => use the script getPolicies.py"
folder_id="folder_id => use the script getFolders.py"
scan_name="Name of the scan"
nessus_url = 'https://127.0.0.1:8834'
access_key = 'ACCESS_KEY created in the Nessus interface'
secret_key = 'SECRET_KEY created in the Nessus interface'
ip_ranges_file = "FILE WITH IP/IPRanges to scan"
############################################################################
headers = {'Content-type': 'application/json', 'X-ApiKeys': 'accessKey='+access_key+'; secretKey='+secret_key}

#GET IPs to scan
IPsList = open(ip_ranges_file, 'r')

#Create scan
data = {
        "uuid": policy_template_id,
        "settings": {
        "name": scan_name,
        "description": "Discovery Scan based on Host enumeration. Ping hosts using: TCP/ARP/ICMP (2 retries)",
        "enabled": "false",
        "launch": "ON_DEMAND",
        "folder_id": folder_id,
        "policy_id": policy_id,
        "text_targets": IPsList,
        }
}

requests.packages.urllib3.disable_warnings()
req = requests.request('POST', nessus_url+'/scans', headers=headers, data=json.dumps(data), verify=False)
data = req.json()
for key, value in data.items():
	for item in value.items():
		if str(item[0]) == "id":
			sid=str(item[1])

#Launch scan
requests.packages.urllib3.disable_warnings()
req = requests.request('POST', nessus_url+'/scans/'+sid+'/launch', headers=headers, verify=False)
data = req.json()
print data
