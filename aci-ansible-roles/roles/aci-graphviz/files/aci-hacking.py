#!/usr/bin/env python
import json

json_file = open('/Github/aci-ansible/aci-ansible-roles/roles/aci-graphviz/files/ACI-RESULTS.JSON')
json_file_str = json_file.read()
json_file_data = json.loads(json_file_str)



#json_file_data['current'][0]['fvAp']['children'][0]['fvAEPg']['attributes']['name']

#for key loop finds all keys at position 0, I can get count of that key occurence from that
#for key in json_file_data['current'][0]:
#   print ( '%s' % key)
#   AppProfileNames = []
#   AppProfileNames.append(key)

#for key loop finds all keys at position 0, I can get count of that key occurence from that
#EPGCounter = (len(json_file_data['current'][0]['fvAp']['children']) - 1)
#for key in json_file_data['current'][0]['fvAp']['children'][0]['fvAEPg']['attributes']['name']:
#   EPGNames = []
#   EPGNames.append(key)
#
#print EPGNames



list = json_file_data['current'][0]['fvAp']['children']
EPG_Name = []
BD_Name = []
for item in list:
    #NewEPG = item['fvAEPg']['attributes']['name']
    EPG_Name.append(item['fvAEPg']['attributes']['name'])

for EPG in EPG_Name:
    #EPG = EPG #json_file_data['current'][0]['fvAp']['children'][EPG_Name.index(EPG)]['fvAEPg']['attributes']
    BD_Name = list[EPG_Name.index(EPG)]['fvAEPg']['children'][0]['fvRsBd']['attributes']['tnFvBDName']
    print BD_Name
    print EPG
