#!/usr/bin/env python

#must pip install graphviz and sudo apt-get install graphviz

from graphviz import Digraph
import json

json_file = open('/Github/aci-ansible/aci-ansible-roles/roles/aci-graphviz/files/ACI-RESULTS.JSON')
json_file_str = json_file.read()
json_file_data = json.loads(json_file_str)

AciView = Digraph(comment='ACI View')

#EPGlist = ("Prod", "Dev", "Test")
#Cxlist = ("WebCx", "DBCx" )

#for EPG in EPGlist:
#    AciView.node( '%s' % EPG, shape='box')
#
#for Cx in Cxlist:
#    AciView.node( '%s' % Cx, shape='oval')

#AciView.edges([ ('ProdWebCx', 'ProdDBCx'), ])
#AciView.edge( 'Web-Cx', 'Dev')
#AciView.edge( 'Web-Cx', 'Test')


#json_file_data['current'][0]['fvAp']['children'][0]['fvAEPg']['attributes']['name']
#for key loop finds all keys at position 0, I can get count of that key occurence from that
#for key in json_file_data['current'][0]:
#   print ( '%s' % key)

with AciView.subgraph(name='cluster0') as ANP:
    ANP.attr(style='filled')
    ANP.attr(color='lightgrey')
    ANP.node_attr.update(style='filled', color='white')
    ANP.attr(label=json_file_data['current'][0]['fvAp']['attributes']['name'])

    list = json_file_data['current'][0]['fvAp']['children']
    EPG_Name = []
    for item in list:
        #NewEPG = item['fvAEPg']['attributes']['name']
        EPG_Name.append(item['fvAEPg']['attributes']['name'])

    for EPG in EPG_Name:
        BD_Name = list[EPG_Name.index(EPG)]['fvAEPg']['children'][0]['fvRsBd']['attributes']['tnFvBDName']
        ANP.edge( '%s'  % EPG, BD_Name )

AciView.render('aciview.gv')


