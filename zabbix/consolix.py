from pprint import pprint
from zabbix_api import ZabbixAPI
import json
import datetime
import getpass

zsvr = str(input('Insira o server: '))
username = str(input('Insira o usuario: '))
password = str(getpass.getpass('Insira a senha: '))

#instanciando a API
conexao = ZabbixAPI(server = zsvr)
conexao.login(username, password)

#lendo versao
versao = conexao.api_version()
print ("Versão do Zabbix Server: ", versao)




hostgroup = conexao.hostgroup.get({"output": "extend", "sortfield": "name"})
for x in hostgroup: #vendo os grupos de host
    print (x['groupid'], "-", x['name'])




y = int(input('Insira o GroupID: '))



groupid=y


#com o id do grupo de host acessa as triggers ativas do grupo
triggerDis = conexao.trigger.get({ "output": "extend",
                                "groupids": groupid,
                                "expandDescription": 1,
                                "filter":{ "value": 1, "priority": 5, "active": 0},
                                "sortfield": "lastchange", "sortorder": "DESC", "monitored": 0
                                })

triggerWar = conexao.trigger.get({ "output": "extend",
                                "groupids": groupid,
                                "expandDescription": 1,
                                "filter":{ "value": 1, "priority": 2, "active": 0},
                                "sortfield": "lastchange", "sortorder": "DESC", "monitored": 0
                                })

triggerInfo = conexao.trigger.get({ "output": "extend",
                                "groupids": groupid,
                                "expandDescription": 1,
                                "filter":{ "value": 1, "priority": 1, "active": 0},
                                "sortfield": "lastchange", "sortorder": "DESC", "monitored": 0
                                })

print("_____________________________")
print("Quantidade de Desastres: %i" % len(triggerDis))
for z in triggerDis:
    print (z['description'])
print("_____________________________")
print("Quantidade de Warnings: %i" % len(triggerWar))
for z in triggerWar:
    print (z['description'])
print("_____________________________")
print("Quantidade de Informações: %i" % len(triggerInfo))
for z in triggerInfo:
    print (z['description'])
print("_____________________________")