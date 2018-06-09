import json
import requests
from bs4 import BeautifulSoup

resp = requests.get(
    'http://exam.cusat.ac.in/erp5/cusat/Cusat-Home/home_oldresults#')
soup = BeautifulSoup(resp.content, "html.parser")

pr = soup.find_all('form')
options = []
for f in pr:
    try:
        sem = f.find_all('input', {'name': 'sem'})[0]['value']
        month = f.find_all('input', {'name': 'month'})[0]['value']
        year = f.find_all('input', {'name': 'year'})[0]['value']
        dn = f.find_all('input', {'name': 'dn'})[0]['value']
        reg_type = f.find_all('input', {'name': 'reg_type'})[0]['value']
        if sem == '1&2':
            sem = '1%262'
        option = [ str(sem), str(month), str(year), str(reg_type), str(dn ) ]
        options.append(option)
    except:
        pass

open('./options.json', 'w').write(json.dumps({ 'options': options }))
