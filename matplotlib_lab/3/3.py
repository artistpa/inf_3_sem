import matplotlib.pyplot as plt
import csv
import pandas as pd

with open('preps.csv') as f1:
    r1 = csv.reader(f1)
    preps = []
    for line in r1:
          preps.extend(line)

with open('groups.csv') as f1:
    r1 = csv.reader(f1)
    groups = []
    for line in r1:
          groups.extend(map(int, line))

with open('marks.csv') as f1:
    r1 = csv.reader(f1)
    marks = []
    for line in r1:
          marks.extend(map(int, line))

fig, axs = plt.subplots(1,7)
labels = '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'
count_marks1 = [0] * 10
for i in range(len(marks)):
    if preps[i] == 'prep1':
        count_marks1[marks[i] - 1] += 1
count_marks2 = [0] * 10
for i in range(len(marks)):
    if preps[i] == 'prep2':
        count_marks2[marks[i] - 1] += 1
count_marks3 = [0] * 10
for i in range(len(marks)):
    if preps[i] == 'prep3':
        count_marks3[marks[i] - 1] += 1
count_marks4 = [0] * 10
for i in range(len(marks)):
    if preps[i] == 'prep4':
        count_marks4[marks[i] - 1] += 1
count_marks5 = [0] * 10
for i in range(len(marks)):
    if preps[i] == 'prep5':
        count_marks5[marks[i] - 1] += 1
count_marks6 = [0] * 10
for i in range(len(marks)):
    if preps[i] == 'prep6':
        count_marks6[marks[i] - 1] += 1
count_marks7 = [0] * 10
for i in range(len(marks)):
    if preps[i] == 'prep7':
        count_marks7[marks[i] - 1] += 1

axs[0].pie(count_marks1, autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '', textprops={'size': 'smaller'}, radius=1.5)
axs[1].pie(count_marks2, autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '', textprops={'size': 'smaller'}, radius=1.5)
axs[2].pie(count_marks3, autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '', textprops={'size': 'smaller'}, radius=1.5)
axs[3].pie(count_marks4, autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '', textprops={'size': 'smaller'}, radius=1.5)
axs[4].pie(count_marks5, autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '', textprops={'size': 'smaller'}, radius=1.5)
axs[5].pie(count_marks6, autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '', textprops={'size': 'smaller'}, radius=1.5)
axs[6].pie(count_marks7, autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '', textprops={'size': 'smaller'}, radius=1.5)

patches, texts = axs[6].pie(count_marks7)
plt.legend(patches, labels, bbox_to_anchor=(2, 2), prop={'size':14})


for i in range(7):
    k = i + 1
    axs[i].set_title(f"prep{k}", fontsize = 10, pad = 14)

plt.show()

df = pd.read_csv("students.csv", delimiter=';')
print(df[df['marks'] == 3].count())
print(df)