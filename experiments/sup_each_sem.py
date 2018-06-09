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


# plt.bar(range(len(marks['1%262'])), marks['1%262'], label='first and second')
# plt.plot(range(len(marks['3'])), marks['3'], label='third')
# plt.plot(range(len(marks['4'])), marks['4'], label='fourth')
plt.bar([key for key in sp_count], sp_list, label='sup')
plt.xlabel('year')
plt.ylabel('sups')
plt.title("Experiment")
plt.legend()
plt.show()
