import matplotlib.pyplot as plt
import numpy as np

languages = ('Spanish', 'French', 'Italian', 'German', 'Chinese', 'Japanese', 'Korean', 'SE Asian', 'Indian', 'Native American')
index = np.arange(len(languages))
speakers = []
english = [] #less than very well or very well?

fig1, ax = plt.subplots()

graph1 = plt.bar(index, speakers, align='center', alpha=0.5)
plt.xticks(index, languages)
plt.xlabel('Language Group')
plt.ylabel('Number of People Who Speak at Home')
plt.title('Languages Spoken at Home in the US, 2009-2013')

plt.show()

fig1, ax = plt.subplots()

graph2 = plt.bar(index, english, align='center', alpha=0.5)
plt.xticks(index, languages)
plt.xlabel('Language Group')
plt.ylabel('Percentage of People Who Speak English "Very Well"')
plt.title('English Ability by Language, 2009-2013')

plt.show()