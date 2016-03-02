from jira import JIRA
import yaml

#Parses config.yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


#Prints parsed variables

#print(cfg['servercfg']['server'])
#print(cfg['servercfg']['user'])
#print(cfg['servercfg']['pwd'])



options = {
    'server': cfg['servercfg']['server'],
}


jira = JIRA(options, basic_auth=(cfg['servercfg']['user'],cfg['servercfg']['pwd']))

print("connected")

issue_dict = {
    'project': 'SD',
    'summary': 'New issue from jira-python',
    'description': 'Look into this one',
    'issuetype': {'name': 'Incidente'},
    'customfield_12100': 'Zabbix',
    'customfield_12106': '4',
    'customfield_12107': '32',
    'customfield_12108': '224',
    'customfield_11402': '9999',

}
new_issue = jira.create_issue(fields=issue_dict)

print(new_issue)

#Elemento 12108 = 224
#Descrição do Serviço  12107= 32
#Categoria 12106 = 4
#Solicitante 12100
