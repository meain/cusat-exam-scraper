import json

data = json.loads(open('./final.txt').read())['data']

name = 'ABIN SIMON'

peruser = {}

for item in data:
    if item['name'] not in peruser:
        peruser[item['name']] = []
    peruser[item['name']].append(item)
