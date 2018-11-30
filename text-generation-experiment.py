'''
Let's make a bunch of fake words
'''
import random
from random import randint

consonants = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z")
vowels = ("a","e","i","o","u","y")

#get a random vowel (or two)
def getVowel(probabilityDouble = 20):
    v=''
    
    v_num = 1
    if randint(0,100) < probabilityDouble:
        v_num = 2
    
    for i in range(randint(1,2)):
        v+=random.choice(vowels)
    return v
	
#get a random consonant
def getConsonant(probabilityDouble = 10):
    c=''
    
    c_num = 1
    if randint(0,100) < probabilityDouble:
        c_num = 2
    
    
    for i in range(c_num):
        c+=random.choice(consonants)
    return c
	
#generate a consonant+vowel or a vowel+consonant pattern
def getSyllable(doubleConsonant=5,doubleVowel=40):
    s=''
    i=random.randint(0,1)
    if i==0:
        s=getVowel(doubleVowel)+getConsonant(doubleConsonant) #V+C
    elif i==1:
        s=getConsonant(doubleConsonant)+getVowel(doubleVowel) #C+V
    return s

def generateListOfSyllables(MaxSyllables = 50, doubleConsonant=5, doubleVowel=40):
    syllables = []
    while len(syllables) < MaxSyllables:
        syllable = getSyllable(doubleConsonant,doubleVowel)
        if syllable not in syllables:
            syllables.append(syllable)
        
    return syllables
    
def generateWordFromSyllables (listOfSyllables, MinSyllables=2, MaxSyllables=6, allowConsonant=0, allowVowel=0):
    word = ""
    for i in range( randint(MinSyllables,MaxSyllables) ):
        word += random.choice(listOfSyllables)
        
        randConsonant = randint(0,100)
        if randConsonant < allowConsonant:
            word += getConsonant(0)
        
        randVowel = randint(0,100)
        if randVowel< allowVowel:
            word += getVowel(0)
            
        
    return word
    
def generateListOfWords(wordsMax, listOfSyllables, MinSyllables=2, MaxSyllables=5, allowConsonant=0, allowVowel=0):
    words = []
    while len(words) < wordsMax:
        word = generateWordFromSyllables (listOfSyllables, MinSyllables, MaxSyllables, allowConsonant, allowVowel)
        if word not in words:
            word = word.capitalize()
            words.append(word)
        
    return words
    

listSyllables = generateListOfSyllables(24,1,1)
listWords = generateListOfWords(20,listSyllables,2,3,3,1)  


while True:
    print("Select the action you want to take:")
    print("\tGenerate New List of Syllables [N]")
    print("\tView current List of Syllables [V]")
    print("\tGenerate Word list from Syllables [W]")
    print("\tEnd Program [Q]")
    
    userSelect = input() 
    print()
    if userSelect.lower() in list('nvwq'):
        #valid command
        
        if userSelect.lower() == 'q':
            #quit program
            break
            
        elif userSelect.lower() == 'n':
            #generate a new list of syllables
            numberSyllables = 10
            while True:
                print("How many syllables to generate?")
                numberSyllables = int( input() )
                if type(numberSyllables) is int:
                    break
                else:
                    print("numbers, please")
                
            listSyllables =generateListOfSyllables(numberSyllables,1,1)
            
        elif userSelect.lower() == 'v':
            #print current list of syllables
            print("SYLLABLES: ")
            print(", ".join(listSyllables))
            print()
            
        elif userSelect.lower() == 'w':
            #generate a new list of words
            numberWords = 5
            while True:
                print("How many words would you like?")
                numberWords = int( input() )
                if type(numberWords) is int:
                    break
                else:
                    print("numbers, please")
            listWords = generateListOfWords(20,listSyllables,2,3,3,1)  
            print("WORDS: ")
            print(", ".join(listWords))
            print()
        
    else:
        #invalid command
        print("That's not one of the valid options, sorry")
    
