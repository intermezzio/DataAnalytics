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
    
    #retrieve all speakers
    for i in range(8,183): # Omit header lines
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
    
    datafile.close()
    
    return languages_data

def line_parser1(data,i):
    '''
    Function to parse data for first question
    Returns a String and a float
    String language = uppercase language
    Float speakers = number of people who speak that language
    '''
    #split data
    lst = data[i].split(',')
    language = lst[0] #get language
    
    speakers = 0 #keep track of number of speakers
    
    n = 0 #counter
            
    while True: #get number of speakers
        if '.00' in lst[n]:
            speakers = float(lst[n])
            n=0
            break
        else:
            n += 1
            
    #format language String               
    language = language.upper()
    language = language.strip('\"')
    language = language.strip('.')
    if '(' in language:
        language = language[:language.find('(')]
    language = language.strip()
    
    return language, speakers

def second_question():
    '''
        Function to retrieve data for Second Question
        Returns the percentage of people in the United States who speak English well out of all bilingual people
        Returns in form of dictionary with the key as uppercase language (String) and the value as the percentage of speakers (float)
        Ex. {"FRENCH",50.0}
    '''
    #openDataFile
    datafile = open('2009-2013-languages-spoken-at-home-ability-to-speak-english-united-states.csv','r')
    data = datafile.readlines()
    
    #declare dictionaries
    total_speakers = first_question()
    speak_english_well_data = {}
    Southeast_well_data={}
    Indian_well_data={}
    Native_American_well_data={}
    
    #lines to collect data from
    languages=[8,13,18,22,95,104,105]
    Southeast_Asian_languages=[106,108,109,110,132]
    Indian_languages=[55,56,57,58,122,123,124,125,127,128]
    Native_American_languages=[181,182]
    
    #retrieve number who speak english well
    for i in range(8,183): # Omit header lines
        if i in languages:
            language, speakers = line_parser2(data,i)
            speak_english_well_data[language] = speakers
            
        if i in Southeast_Asian_languages:
            language, speakers = line_parser2(data,i)
            Southeast_well_data[language] = speakers
        
        if i in Indian_languages:
            language, speakers = line_parser2(data,i)
            Indian_well_data[language] = speakers
        
        if i in Native_American_languages:
            language, speakers = line_parser2(data,i)
            Native_American_well_data[language] = speakers
    
    #consolidate Southeast Asian Languages
    total_well = 0
    
    for language in Southeast_well_data:
        total_well += float(Southeast_well_data[language])
            
    speak_english_well_data['SOUTHEAST ASIAN LANGUAGES'] = total_well
    
    #consolidate Indian Languages
    total_well = 0
    
    for language in Indian_well_data:
        total_well += float(Indian_well_data[language])
            
    speak_english_well_data['INDIAN LANGUAGES'] = total_well
    
    #consolidate Native American Languages
    total_well = 0
    
    for language in Native_American_well_data:
        total_well += float(Native_American_well_data[language])
            
    speak_english_well_data['NATIVE AMERICAN LANGUAGES'] = total_well
    
    #make dictionary of percentages
    percentages = {}
    for language in total_speakers:
        percent = speak_english_well_data[language] / (total_speakers[language] * 0.01)
        percentages[language] = percent
    
    datafile.close()
    
    return percentages

def line_parser2(data,i):
    '''
    Function to parse data for second question
    Returns a String and a float
    String language = uppercase language
    Float speakers = number of people who speak that language speak English well language
    '''
    #split data
    lst = data[i].split(',')
    language = lst[0] #get language
    
    #keep track of number of speakers who speak english well
    speakers = 0
    
    n = 0 #counter
        
    #get number of speakers who speak english well     
    while True:
        if '.00' in lst[n]:
            speakers = float(lst[n+2]) #the number who speak english well is two columns down from the first number
            n=0
            break
        else:
            n += 1
             
    #format language String                       
    language = language.upper()
    language = language.strip('\"')
    language = language.strip('.')
    if '(' in language:
        language = language[:language.find('(')]
    language = language.strip()
    
    return language, speakers

def third_question():
    '''
        Function to retrieve data for Third Question
        Returns the percentage of people in each state who speak another language who speak english well
        Returns in form of dictionary with the key as state (String) and the value as the percentage of people who speak english well (float)
        Ex. {"New Jersey",50.0}
    '''
    #list of states
    states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District_of_Columbia',
                'Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland',
                'Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New_Hampshire',
                'New_Jersey','New_Mexico','New_York','North_Carolina','North_Dakota','Ohio','Oklahoma','Oregon','Pennsylvania',
                'Puerto_Rico','Rhode_Island','South_Carolina','South_Dakota','Tennessee','Texas','Utah','Vermont','Virginia',
                'Washington','West_Virginia','Wisconsin','Wyoming']
    
    #states = ['Alabama','Alaska', 'Arizona', 'Arkansas', 'California', 'Connecticut']
    
    bilingual_people = {}
    speak_english_well = {}
    percentages = {}
    
    for state in states:
        #openDataFile
        with open(state + '.csv','r') as datafile:
            
            data = datafile.readlines()
            
            state_name = state.replace('_',' ')
            
            bilingual, well = bilingual_people_by_state(data, False)
            bilingual_people[state_name] = bilingual
            speak_english_well[state_name] = well
            
    for state in bilingual_people:
        percentages[state] = 100 - (speak_english_well[state] / (bilingual_people[state] * 0.01))
    
    print speak_english_well
    print bilingual_people
    return percentages

def fourth_question():
    '''
        Function to retrieve data for Fourth Question
        Returns the percentage of people in each state who speak a second language
        Returns in form of dictionary with the key as state (String) and the value as the percentage of speakers (float)
        Ex. {"New Jersey",75.0}
    '''
    #list of states
    states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District_of_Columbia',
                'Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland',
                'Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New_Hampshire',
                'New_Jersey','New_Mexico','New_York','North_Carolina','North_Dakota','Ohio','Oklahoma','Oregon','Pennsylvania',
                'Puerto_Rico','Rhode_Island','South_Carolina','South_Dakota','Tennessee','Texas','Utah','Vermont','Virginia',
                'Washington','West_Virginia','Wisconsin','Wyoming']
    
    bilingual_people = {}
    total_people = {}
    percentages = {}
    
    for state in states:
        #openDataFile
        with open(state + '.csv','r') as datafile:
            
            data = datafile.readlines()
            
            state_name = state.replace('_',' ')
            
            bilingual, total = bilingual_people_by_state(data, True)
            bilingual_people[state_name] = bilingual
            total_people[state_name] = total
            
    for state in bilingual_people:
        percentages[state] = bilingual_people[state] / (total_people[state] * 0.01)
    
    print total_people
    print bilingual_people
    return percentages      

def bilingual_people_by_state(data, total):
    '''
    Function to return the number of bilingual people by state, and a second value that depends on total
    Returns two floats
    Float = number of bilingual people in the state
    
    If total = True, the second float = total population of state
    If total = False, the second float = total people who speak English well
    '''
    #split data
    lst = data[7].split(',')
    
    #keep track of number of bilingual people and second variable
    speakers = 0
    speakers2 = 0
    
    n = 0 #counter
        
    #get number of bilingual people   
    while True:
        if '.00' in lst[n]:
            speakers = float(lst[n])
            n=0
            
            if not total:
                #number of people who speak english well
                speakers2 = float(lst[n+3])
            
            break
            
        else:
            n += 1
    
    n = 0
        
    if total:
        #total number of people
        lst = data[5].split(',')
        while True:
            if '.00' in lst[n]:
                speakers2 = float(lst[n])
                n=0
            
                break
            
            else:
                n += 1
    
    n = 0
    
    return speakers, speakers2