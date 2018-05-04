import matplotlib.pyplot as plt
import numpy as np
from ReadingData import *

q1 = first_question()
q2 = second_question()
#format long labels by splitting words onto new lines
for dict in (q1, q2):
    for key in dict:
        if ' ' in key:
            new_key = '\n'.join(key.split(' '))
            dict[new_key] = dict[key]
            del dict[key]
index = np.arange(len(q1.keys()))
#convert from "less than very well" to "very well"
english = []
for value in q2.values():
    english.append(100-value)

#first question bar graph
fig1, ax1 = plt.subplots()
graph1 = plt.bar(index, q1.values(), align='center', alpha=0.5)
plt.xticks(np.arange(len(q1.keys())), q1.keys())
plt.xlabel('Language Group')
plt.ylabel('Number of People Who Speak at Home')
ax1.set_yscale('log') #set to log scale
plt.title('Languages Spoken at Home in the US, 2009-2013')
plt.show()

#second question bar graph
fig1, ax2 = plt.subplots()
graph2 = plt.bar(index, english, align='center', alpha=0.5)
plt.xticks(np.arange(len(q2.keys())), q2.keys())
plt.xlabel('Language Group')
plt.ylabel('Percentage of People Who Speak English "Very Well"')
plt.ylim(ymax=100) #set max of y axis to 100%
plt.title('English Ability by Language, 2009-2013')
plt.show()