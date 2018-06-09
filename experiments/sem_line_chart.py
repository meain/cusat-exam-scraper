import json
import matplotlib.pyplot as plt

data = json.loads(open('./final.txt').read())['data']

marks = {}
sp_count = {}
for el in data:
    if el['sem'] not in marks:
        marks[el['sem']] = []
        sp_count[el['sem']] = 0
    if el['exam'] == 'Regular':
        if el['gpa'] == -1:
            sp_count[el['sem']] += 1
        marks[el['sem']].append(el['gpa'] if el['gpa'] != -1 else 0)

sp_list = []
for el in sp_count:
    sp_list.append(sp_count[el])

plt.plot(range(len(marks['1%262'])), marks['1%262'], label='first and second')
plt.plot(range(len(marks['3'])), [m + 15 for m in marks['3']], label='third')
plt.plot(
    range(len(marks['4'])), [m + 2 * 15 for m in marks['4']], label='fourth')
plt.plot(
    range(len(marks['5'])), [m + 3 * 15 for m in marks['5']], label='fifth')
plt.plot(
    range(len(marks['6'])), [m + 4 * 15 for m in marks['6']], label='sixth')
plt.plot(
    range(len(marks['7'])), [m + 5 * 15 for m in marks['7']], label='seventh')
plt.plot(
    range(len(marks['8'])), [m + 6 * 15 for m in marks['8']], label='eighth')

# plt.grid(color='g', linestyle='-', linewidth=.1)
plt.xlabel('class')
plt.ylabel('gpa')
plt.title("Experiment")
plt.legend()
plt.show()
