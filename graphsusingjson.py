# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RsXg0ZOJcKi9rIU-u7Ig4c2hxIEogrE0
"""

import matplotlib.pyplot as plt
import json
from datetime import datetime

f=open('temprature.json')
data=json.load(f)

data

dates=[]
temperature=[]
for i in range(len(data)):
  dates.append(data[i]['date'])
  temperature.append(data[i]['temperatureC'])
dates

for i in range(len(dates)):
  dates[i]=datetime.strptime(dates[i],'%Y-%m-%d')
dates

plt.plot(dates,temperature)
plt.title('Dates vs Temperature')
plt.xlabel('Dates')
plt.ylabel('Temperature')
plt.show()