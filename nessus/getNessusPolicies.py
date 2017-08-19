#!/usr/bin/env python2.7
import requests

#########################################
# SETTINGS                              #
#########################################
nessus_url = 'https://127.0.0.1:8834'
access_key = 'ACCESS_KEY created in the Nessus interface'
secret_key = 'SECRET_KEY created in the Nessus interface'
#########################################
headers = {'Content-type': 'application/json', 'X-ApiKeys': 'accessKey='+access_key+'; secretKey='+secret_key}
requests.packages.urllib3.disable_warnings()
req = requests.request('GET', nessus_url+'/policies', headers=headers, verify=False)
data = req.json()
for key, value in data.items():
    for policy in value:
        print "Policy: " + str(policy['name']) + " -> id = " + str(policy['id']) + " -> template_id = " +str(policy['template_uuid'])
