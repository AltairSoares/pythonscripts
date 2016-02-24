from jira import JIRA
import yaml

#Parses config.yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


#Prints parsed variables

print(cfg['servercfg']['server'])
print(cfg['servercfg']['user'])
print(cfg['servercfg']['pwd'])



options = {
    'server': cfg['servercfg']['server'],
}


jira = JIRA(options, basic_auth=(cfg['servercfg']['user'],cfg['servercfg']['pwd']))

print("connected")
print(projects = jira.projects())

'''issue_dict = {
    'project': {'id': 123},
    'summary': 'New issue from jira-python',
    'description': 'Look into this one',
    'issuetype': {'name': 'Bug'},
}
new_issue = jira.create_issue(fields=issue_dict)'''

