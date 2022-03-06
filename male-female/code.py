import pandas as pd
import statistics
import plotly.express as px


from google.colab import files
dataLoad = files.upload()

df = pd.read_csv('data.csv')
fig = px.scatter(df, y = 'quant_saved', color = 'rem_any')
fig.show()

import csv
import plotly.graph_objects as pg

with open('data.csv', newline = '') as f:
    reader  = csv.reader(f)
    data = list(reader)

data.pop(0)


totalEntries = len(data)

reminder = 0

for i in data:
    if int(i[3]) == 1:
        reminder += 1

fig = pg.Figure(pg.Bar(x = ['reminded', 'not reminded'], y = [reminder, totalEntries - reminder]))

fig.show()


allSavings = []

for a in data:
    allSavings.append(float(a[0]))

mean = statistics.mean(allSavings)
print(mean)

median = statistics.median(allSavings)
print(median)

mode = statistics.mode(allSavings)
print(mode)


notReminded = []
reminded = []

for b in data:
    if int(b[3]) == 1:
        reminded.append(float(b[0]))
    else:
        notReminded.append(float(b[0]))

print("Reminded Peoples Data")
print("Mean", statistics.mean(reminded))
print("Median", statistics.median(reminded))
print("Mode", statistics.mode(reminded))

print("Not Reminded Peoples Data")
print("Mean", statistics.mean(notReminded))
print("Median", statistics.median(notReminded))
print("Mode", statistics.mode(notReminded))



stdAll = statistics.stdev(allSavings)
print("Std Of All", stdAll)

stdRem = statistics.stdev(reminded)
print("Std Of Rem", stdRem)

stdNot = statistics.stdev(notReminded)
print("Std Of Not Rem", stdNot)
