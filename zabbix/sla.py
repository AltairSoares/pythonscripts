from pprint import pprint
from zabbix_api import ZabbixAPI
import json
import datetime
import getpass
import time
import json
import math


#zsvr = str(input('Insira o server: '))
zsvr = "https://www.tjms.jus.br/zabbix"
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

now=time.mktime(datetime.datetime.now().timetuple())
dias = 180



comeco=now - (60 * 60 * 24 * 7)



hosts = conexao.host.get({"output": "extend", "groupids": groupid})
for x in hosts:
    triggerDis = conexao.event.get({ "output": "extend",
                                "hostids": x,
                                "status": 1,
                                "object": 0,
                                "time_from": comeco,
                                "time_till": now,
                                "selectHosts": ["host", "hostid"],
                                "selectRelatedObject": ["lastchange", "priority", "description"],
                                "sortfield": "clock",
                                "sortorder": "DESC"
                                })
    timestamp_evento_anterior = datetime.datetime.fromtimestamp(int(comeco))
    for z in triggerDis:
        for objk, objv in z['relatedObject'].items():
            if objk == "description":
                if objv.find("Inace") != -1:
                    for hostx in z['hosts']:
                        timestamp_evento_atual = datetime.datetime.fromtimestamp(int(z["clock"]))
                        diferenca = timestamp_evento_anterior -timestamp_evento_atual 
                        if z["value"] == "1" and diferenca > datetime.timedelta(hours=6):
                            status = "Down"
                            print(timestamp_evento_atual, " ", hostx['host']," " ,status, end=' ')
                            print(diferenca.__str__())
                        timestamp_evento_anterior = timestamp_evento_atual


















