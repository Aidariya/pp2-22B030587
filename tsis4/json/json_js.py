import json

with open('sample.json','r') as task:
    j = json.load(task)
print('Interface Status')
print('='*80)
print('DN'," "*48,"Description"," "*9,'Speed'," "*1,'MTU')
print('-'*50,"",'-'*20,"","-"*6,""*2,"-"*6)

for i in j["imdata"]:
    dn = i['l1PhysIf']['attributes']['dn']
    desc = i['l1PhysIf']['attributes'].get('descr', '')
    speed = i['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = i['l1PhysIf']['attributes'].get('mtu', '')
    print(f"{dn:<50} {desc:<20} {speed:>6} {mtu:>6}")
