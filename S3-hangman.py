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
        guess = raw_input('Please guess a letter: ')
        guess.lower()
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
