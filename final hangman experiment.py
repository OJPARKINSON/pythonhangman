Hangman = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   |
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")
firstWord = ()  #These all open strings so that they can all be given letters
secondWord = ()
thirdWord = ()
fourthWord = ()
fithWord = ()
sixthWord = ()
seventhWord = ()
wordLength = 8  #Set up for the while loop
while True:
    print("\t", "Welcome to two player hangman hang man", "\t ")
    while wordLength >= 7:
        word = input("Player one please enter a word for player two to guess word, no longer than 7 letters: ")
        neword = [word[x:x+1] for x in range(0,len(word),1)]  #used to separte the word so that each letter can be assigned a name
        wordLength = len(neword)  #Works out the lenth of the word      
    print((" \n") * 42)  #Seperates the player 1 part with the player 2 part.
    if wordLength == 2:  #Using this if staitment, it gives each letter a name and this is worked out by looking at the letter length.
        firstWord, secondWord = word
        wordDisplay = ["_","_"]  #This sets the number of letters so it is hidden and it can be changed when player 2 guesses it correct.
    elif wordLength  == 3:
        firstWord, secondWord, thirdWord = word
        wordDisplay = ["_","_","_"]  #Has to be set out like this so that its an integer. 
    elif wordLength == 4:
        firstWord, secondWord, thirdWord, fourthWord = word
        wordDisplay = ["_","_","_","_"]
    elif wordLength == 5:
        firstWord, secondWord, thirdWord, fourthWord, fithWord = word
        wordDisplay = ["_","_","_","_","_"]
    elif wordLength == 6:
        firstWord, secondWord, thirdWord, fourthWord, fithWord, sixthWord = word
        wordDisplay = ["_","_","_","_","_","_"]
    elif wordLength == 7:
        firstWord, secondWord, thirdWord, fourthWord, fithWord, sixthWord, seventhWord = word
        wordDisplay = ["_","_","_","_","_","_","_"]
    else:
        print ("The word needs to be between 2-8 letters long")
        break
    print(Hangman[0])
    attempts = len(Hangman) - 1      
    correct_letters = []
    incorrectLetters = ()
    incorrect_guess = 0
    correct_guess = 0  #Sets up for the varibles 
    print(wordLength * "_ ")
    guess = input("Guess a letter :")
    while wordDisplay != neword:
        if guess == firstWord or guess == secondWord or guess == thirdWord or guess == fourthWord or guess == fithWord or guess == sixthWord or guess == seventhWord:
            correct_guess += 1
            print(Hangman[(len(Hangman) - 0) - attempts])
            if guess == firstWord:  #If the players 2 guess equals the first word and then it selects the frist letter in the list and replaces it with guess insted of "_". 
                wordDisplay[0] = guess
            if guess == secondWord:
                wordDisplay[1] = guess
            if guess == thirdWord:  #It uses if staitments so that there are two if the same letter it diesnt have to be guesses twice
                wordDisplay[2] = guess
            if guess == fourthWord:
                wordDisplay[3] = guess
            if guess == fithWord:
                wordDisplay[4] = guess
            if guess == sixthWord:
                wordDisplay[5] = guess
            if guess == seventhWord:
                wordDisplay[6] = guess
            print(" \n " * 3)  #Adds new blank lines
            print(', '.join(wordDisplay))  #Puts the sting togeather
            print("You have ", incorrect_guess, "incorrect guesses")
            print(" \n " * 2)
            if wordDisplay == neword:
            	Print("Well done")
                break    
            elif correct_letters != word:
                guess = input("Have another guess: ")
                pass
            if incorrect_guess == 10:
                print("You have reached the maximum incorrect guesses:", incorrect_guess, "Unlucky press y below to have another game")
                break
        else:
            incorrect_guess += 1
            print("Incorect guess, you have", incorrect_guess, "incorrect guesses")
            if incorrect_guess == 10:
            	print("Unlucly, you've reached the max ammount of wrong guesses")
            	break
            attempts -= 1
            print(Hangman[(len(Hangman) - 1) - attempts])
            print(', '.join(wordDisplay), " \n")  #prints the list without the separation
            if correct_guess == wordLength:
                print("Well done, you guessed the worddd")
                print(Hangman[(len(Hangman) - 0) - attempts])
                break
            elif correct_letters != word:
                guess = input("Have another guess: ")                   
    print(" \n ")
    print("The word was: ", word)
    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':  #Add player swap
        print(" \n " * 10)
        print("Now player one is player two and player two is now player one")
        continue
    else:
        print('Goodbye')
        break
