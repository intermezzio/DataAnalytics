import matplotlib.pyplot as plt
import csv

def first_question():
    '''
        Function to retrieve data for First Question
        Returns the number of people in the United States who speak each language
        Returns in form of dictionary with the key as uppercase language and the value as the number of speakers
        Ex. {"FRENCH",3000.00}
    '''
    #openDataFile
    datafile = open('2009-2013-languages-spoken-at-home-ability-to-speak-english-united-states.csv','r')
    data = datafile.readlines()

    #lines to collect data from
    languages=[8,13,18,22,95,104,105]
    Southeast_Asian_languages=[106,108,109,110,132]
    Indian_languages=[55,56,57,58,122,123,124,125,127,128]
    Native_American_languages=[181,182]
    
    #declare dictionaries
    languages_data={}
    Southeast_Asian_languages_data={}
    Indian_languages_data={}
    Native_American_languages_data={}
    
    n = 0 #counter
    
    #retrieve data
    for i in range(8,183): # Omit header lines
        if i in languages:
            lst = data[i].split(',')
            language = lst[0]
            
            while True:
                if '.00' in lst[n]:
                    speakers = lst[n]
                    n=0
                    break
                else:
                    n += 1
                    
            language = language.upper()
            language = language.strip()
            language = language.strip('\"')
            language = language.strip('.')
            if '(' in language:
                language = language[:language.find('(')]
            
            languages_data[language] = speakers
    
    return languages_data
