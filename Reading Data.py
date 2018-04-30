import matplotlib.pyplot as plt

datafile = open('insert_filename_here.csv','r')
data = datafile.readlines()

ages=[]
for line in data[3:]: # Omit header lines
    age, income = line.split(',')
    ages.append(int(age))