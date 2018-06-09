import json
import aiohttp
import asyncio
import traceback
from bs4 import BeautifulSoup

url = 'http://exam.cusat.ac.in/erp5/cusat/CUSAT-RESULT/Result_Declaration/display_sup_result'
headers = {
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":
    "gzip, deflate",
    "Accept-Language":
    "en-US,en;q=0.9",
    "Cache-Control":
    "no-cache",
    "Connection":
    "keep-alive",
    "Content-Type":
    "application/x-www-form-urlencoded",
    "Origin":
    "http://exam.cusat.ac.in",
    "Pragma":
    "no-cache",
    "Referer":
    "http://exam.cusat.ac.in/erp5/cusat/CUSAT-RESULT/latest_uni_result/rresult1",
    "Upgrade-Insecure-Requests":
    "1",
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
}


def get_data(reg_no,
             month='April',
             year=2018,
             exam='Regular',
             semester=8,
             deg='B.Tech'):
    return f"regno={reg_no}&deg_name={deg}&semester={semester}&month={month}&year={year}&result_type={exam}"


scraped_data = []


async def fetch(session, url, data):
    async with session.post(url, data=data, headers=headers) as response:
        return await response.text()


async def fetch_result(reg_no,
                       month='April',
                       year=2018,
                       exam='Regular',
                       semester=8,
                       deg='B.Tech'):
    async with aiohttp.ClientSession() as session:
        try:
            global data

            data = get_data(
                reg_no, semester=semester, month=month, year=year, exam=exam)
            html = await fetch(session, url, data=data)
            soup = BeautifulSoup(html, "html.parser")
            name = soup.find_all('table')[0].findAll("tr")[0].findAll("td")[
                1].text
            marks_table = soup.find_all('table')[1].findAll("tr")
            results = []
            for item in marks_table[1:]:
                items = item.find_all('td')
                result = {
                    'code': items[0].text,
                    'subject': items[1].text,
                    'marks': items[2].text.split('(')[0][2:],
                    'grade': items[2].text.split('(')[1].split(')')[0],
                    'passed': True
                    if items[3].text[1:-1] == 'PASSED' else False
                }
                results.append(result)
            others = soup.find_all('body')[0].text.split('\n')[-15:-8]
            total = -1
            gpa = -1
            cgpa = -1
            classification = ''
            for item in others:
                if len(item.split(':')) == 2 and not (
                        item.split(':')[1] == '' or item.split(':')[1] == ' '):
                    if 'Total :' in item:
                        total = int(float(item.split(':')[1] + '.0'))
                    if 'GPA   :' in item:
                        gpa = float(item.split(':')[1])
                    if 'CGPA\xa0:' in item:
                        cgpa = float(item.split(':')[1][1:])
                    if 'Classification\xa0:' in item:
                        classification = item.split(':')[1][1:]
            student = {
                'name': name,
                'month': month,
                'sem': semester,
                'exam': exam,
                'year': year,
                'reg_no': reg_no,
                'results': results,
                'total': total,
                'gpa': gpa,
                'cgpa': cgpa,
                'classification': classification
            }
            scraped_data.append(student)
            print(name, semester, exam, year)
        except Exception as e:
            # if exam == 'Regular':
            #     print("\t\t\tSkipping:", reg_no, semester, exam, year)
            # print(traceback.format_exc())
            pass


loop = asyncio.get_event_loop()
tasks = []

try:
    options = json.loads(open('./options.json').read())['options']
except:
    print('Run examtypes.py to fetch these')

# for option in options:
#     tasks.append(
#         asyncio.ensure_future(
#             fetch_result(
#                 12150002,
#                 semester=option[0],
#                 month=option[1],
#                 year=option[2],
#                 exam=option[3])))
# tasks.append(asyncio.ensure_future(fetch_result(12150030)))
count = 0
for i in range(12150000, 12150090):
    print(f"\n\n{i}")
    for option in options:
        count += 1
        tasks.append(
            asyncio.ensure_future(
                fetch_result(
                    i,
                    semester=option[0],
                    month=option[1],
                    year=option[2],
                    exam=option[3])))
        if count == 10:
            count = 0
            loop.run_until_complete(asyncio.wait(tasks))
            tasks = []

# print(len(scraped_data), json.dumps(scraped_data))
print(len(scraped_data))
open('test.txt', 'w').write(json.dumps({'data': scraped_data}))
