import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase 
letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

__author__ = 'prance'

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in 
lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that 
represents
      what letters in secretWord have been guessed so far.
    '''
    val=''
    for i in secretWord:
        if i in lettersGuessed:
            val += i
        else:
            val += '_'
    return val

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters 
have not
      yet been guessed.
    '''
    import string as s
    val = ''
    for i in s.ascii_lowercase:
        if i not in lettersGuessed:
            val += i
    return val

def hangman(secretWord):
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' 
letter long.')
    guessesLeft = 8
    lettersGuessed = ''
    while guessesLeft > 0 and isWordGuessed(secretWord, lettersGuessed) 
== False:
        print('-------------')
        print('You have ' + str(guessesLeft) + ' guesses left.')
        print('Available letters: ' + 
getAvailableLetters(lettersGuessed))
        guess = raw_input('Please guess a letter: ').lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:" + 
getGuessedWord(secretWord, lettersGuessed))
        elif guess not in secretWord:
            print('Oops! That letter is not in my word:' + 
getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed += guess
            guessesLeft -= 1
        elif guess in secretWord:
            lettersGuessed += guess
            print('Good guess: ' + getGuessedWord(secretWord, 
lettersGuessed))
    if guessesLeft == 0:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was ' + 
secretWord + '.')
    elif isWordGuessed(secretWord, lettersGuessed) == True:
        print('-------------')
        print('Congratulations, you won!')
    return 0
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
