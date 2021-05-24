#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, time
from datetime import timedelta

import csv

#dataSet = np.genfromtxt('triathalon.csv', skip_header=1, delimiter=',')

f = open('triathalon.csv', 'rb')
reader = csv.reader(f)
headers = reader.next()
print headers
column = {}
for h in headers:
	column[h] = []
#print column
for row in reader:
	for h, v in zip(headers, row):
		column[h].append(v)

age_times = zip(column['AGE'], column['FINALTM'])
age_dict = {}
for age_time in age_times:
	age  = int(age_time[0])
	dt = datetime.strptime(age_time[1], '%H:%M:%S')
	final_time = timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second)
	if not age in age_dict.keys():
		age_dict[age] = [final_time]
	else:
		age_dict[age].append(final_time)

def avg_time(timedeltas):
	seconds_list = [i.total_seconds() for i in timedeltas]
	return sum(seconds_list)/float(len(seconds_list))

age_time_averages = []
# http://stackoverflow.com/questions/12033905/using-python-to-create-an-average-out-of-a-list-of-times
for age, times in age_dict.iteritems():
	age_time_averages.append([age, avg_time(times)])
	print age,':',str(timedelta(seconds=avg_time(times)))

age_time_averages = sorted(age_time_averages)

objects = [i[0] for i in age_time_averages]
y_pos = np.arange(len(objects))
performance = [i[1] for i in age_time_averages]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()