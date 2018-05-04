import matplotlib.pyplot as plt
import numpy as np
from ReadingData import *

'''
Creates bar graphs for first and second questions using matplotlib
'''

#format long labels by splitting words onto new lines
def format_labels(dict):
    for key in dict:
        if ' ' in key:
            new_key = '\n'.join(key.split(' '))
            dict[new_key] = dict[key]
            del dict[key]

def first_graph():
    q1 = first_question()
    format_labels(q1)
    fig, ax = plt.subplots()
    graph = plt.bar(np.arange(len(q1.keys())), q1.values(), align='center', alpha=0.5)
    plt.xticks(np.arange(len(q1.keys())), q1.keys())
    plt.xlabel('Language Group')
    plt.ylabel('Number of People Who Speak at Home')
    ax.set_yscale('log') #set to log scale
    plt.title('Languages Spoken at Home in the US, 2009-2013')
    plt.show()

def second_graph():
    q2 = second_question()
    format_labels(q2)
    #convert from "less than very well" to "very well" by subtracting from 100%
    english = []
    for value in q2.values():
        english.append(100-value)
    fig, ax = plt.subplots()
    graph = plt.bar(np.arange(len(q2.keys())), english, align='center', alpha=0.5)
    plt.xticks(np.arange(len(q2.keys())), q2.keys())
    plt.xlabel('Language Group')
    plt.ylabel('Percentage of People Who Speak English "Very Well"')
    plt.ylim(ymax=100) #set max of y axis to 100%
    plt.title('English Ability by Language, 2009-2013')
    plt.show()
