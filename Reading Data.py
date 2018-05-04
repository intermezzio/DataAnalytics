import matplotlib.pyplot as plt
import csv

def first_question():
    '''
        Function to retrieve data for First Question
        Returns the number of people in the United States who speak each language
        Returns in form of dictionary with the key as uppercase language (String) and the value as the number of speakers (float)
        Ex. {"FRENCH",3000.0}
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
    
    #retrieve data
    for i in range(8,183): # Omit header lines
        #retrieve all languages data
        if i in languages:
            language, speakers = line_parser1(data,i)
            languages_data[language] = speakers
            
        if i in Southeast_Asian_languages:
            language, speakers = line_parser1(data,i)
            Southeast_Asian_languages_data[language] = speakers
        
        if i in Indian_languages:
            language, speakers = line_parser1(data,i)
            Indian_languages_data[language] = speakers
        
        if i in Native_American_languages:
            language, speakers = line_parser1(data,i)
            Native_American_languages_data[language] = speakers
    
    #consolidate Southeast Asian Languages
    total_speakers = 0
    
    for language in Southeast_Asian_languages_data:
        total_speakers += float(Southeast_Asian_languages_data[language])
            
    languages_data['SOUTHEAST ASIAN LANGUAGES'] = total_speakers
    
    #consolidate Indian Languages
    total_speakers = 0
    
    for language in Indian_languages_data:
        total_speakers += float(Indian_languages_data[language])
            
    languages_data['INDIAN LANGUAGES'] = total_speakers
    
    #consolidate Native American Languages
    total_speakers = 0
    
    for language in Native_American_languages_data:
        total_speakers += float(Native_American_languages_data[language])
            
    languages_data['NATIVE AMERICAN LANGUAGES'] = total_speakers
    
    return languages_data

def line_parser1(data,i):
    
    lst = data[i].split(',')
    language = lst[0]
    speakers = 0
    
    n = 0 #counter
            
    while True:
        if '.00' in lst[n]:
            speakers = float(lst[n])
            n=0
            break
        else:
            n += 1
                    
    language = language.upper()
    language = language.strip('\"')
    language = language.strip('.')
    if '(' in language:
        language = language[:language.find('(')]
    language = language.strip()
    
    return language, speakers
