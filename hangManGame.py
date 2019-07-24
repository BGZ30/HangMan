import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print ("  "), (len(wordlist)), ("words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

def isWordGuessed(secretWord, lettersGuessed):
    if lettersGuessed==[]:
        return False
    else:
       for i in range(len(secretWord)):
          if lettersGuessed in secretWord[i]:
               return True
          else:
              x= False
    return x
            

def getGuessedWord(secretWord, lettersGuessed):
    w=[]
    x=''
    i=0
    for i in range(len(secretWord)):
      if secretWord[i] in lettersGuessed:
          w.append(secretWord[i])
      else:
          w.append('_ ')
      x=x+w[i]

    return x


def getAvailableLetters(lettersGuessed):
    LL=''
    L=string.ascii_lowercase
    if lettersGuessed == []:
        return L
    else:
      for i in range(len(L)):
         if L[i] not in lettersGuessed:
             LL=LL+(L[i])
    return LL


def hangman(secretWord):
    lenSw=len(secretWord)
    word='_'*lenSw
    mistakesMade=0
    lettersGuessed=[]
    availableLetters=string.ascii_lowercase
    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is ' + str(lenSw) + ' letters long.')
    print (12*'-')

    while word != secretWord and mistakesMade <8:
       print ('You have ' + str(8-mistakesMade) + ' guesses left.')

       availableLetters = getAvailableLetters(lettersGuessed)   #show left letters

       print ('Available letters: ' + availableLetters)
       print ('Please guess a letter: ') ,

       letter=str(raw_input().lower())
       if letter in lettersGuessed:
          print  ("Oops! You've already guessed that letter: " + word)
          print (12*'-')
       else:   
        lettersGuessed.append(letter)
        word=getGuessedWord(secretWord, lettersGuessed) # show progress
        result=isWordGuessed(secretWord, letter) #check the letter
        if result == True:
          print ('Good guess: ' + word)
          print (12*'-')
        else:
          print ('Oops! That letter is not in my word: ' + word)
          print (12*'-')
          mistakesMade+=1
         
        if word == secretWord:
          print ('Congratulations, you won!')
          break
        elif mistakesMade==8:
            print ('Sorry, you ran out of guesses. The word was ' + secretWord +'.')
  

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord=chooseWord(wordlist)
hangman(secretWord)
