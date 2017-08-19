#!/usr/bin/env python2.7
import requests

#########################################
# SETTINGS                              #
#########################################
nessus_url = 'https://127.0.0.1:8834'
access_key = '232c091c80bfe6bec86906dc4b00ce55e926ab7537236e31b1ffc93ee2939f8a'
secret_key = '3084e3c5dcdf8786178b12955b11dc3b13e5554377410587e48c9e54590d35dc'
#########################################

#Get folders request
headers = {'Content-type': 'application/json', 'X-ApiKeys': 'accessKey='+access_key+'; secretKey='+secret_key}
requests.packages.urllib3.disable_warnings()
req = requests.request('GET', nessus_url+'/folders', headers=headers, verify=False)
data = req.json()
for key, value in data.items():
    for folder in value:
        print "Folder: " + str(folder['name']) + " -> id = " + str(folder['id'])
