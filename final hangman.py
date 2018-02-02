while True:
    firstWord = ()
    secondWord = ()
    thirdWord = ()
    fourthWord = ()
    fithWord = ()
    sixthWord = ()
    seventhWord = ()
    eighthWord = () 
    wordLength = 9 #set up for the while loop
    print("\t Welcome to two player hangman hang man", "\t ")
    while wordLength >= 8:
        word = input("Player one please enter a word for player two to guess word, no longer than 8 letters: ")
        neword = [word[i:i+1] for i in range(0,len(word),1)] #used to separte the word so that each letter can be assigned a name
        wordLength = len(neword) #Works out the lenth of the word      
    print((" \n") * 40)  #seperates the player 1 part with the player 2 part.
    print((" \n") * 2) 
    if wordLength == 2:  #Using this if staitment, it gives each letter a name and this is worked out by looking at the letter length.
        firstWord, secondWord = word
        print(word)
        lenth_number = 2
        newwword = ["_","_"]  #this sets the number of letters so it is hidden and it can be changed when player 2 guesses it correct.
    elif wordLength  == 3:
        firstWord, secondWord, thirdWord = word
        lenth_number = 3
        newwword = ["_","_","_"]
    elif wordLength == 4:
        firstWord, secondWord, thirdWord, fourthWord = word
        lenth_number = 4
        newwword = ["_","_","_","_"]
    elif wordLength == 5:
        firstWord, secondWord, thirdWord, fourthWord, fithWord = word
        lenth_number = 5
        newwword = ["_","_","_","_","_"]
    elif wordLength == 6:
        firstWord, secondWord, thirdWord, fourthWord, fithWord, sixthWord = word
        lenth_number = 6
        newwword = ["_","_","_","_","_","_"]
    elif wordLength == 7:
        firstWord, secondWord, thirdWord, fourthWord, fithWord, sixthWord, seventhWord = word
        lenth_number = 7
        newwwordunderline = ["_","_","_","_","_","_","_"]
    elif wordLength == 8:
        firstWord, secondWord, thirdWord, fourthWord, fithWord, sixthWord, seventhWord, eighthWord = word
        lenth_number = 8
        newwword = ["_","_","_","_","_","_","_","_"]
    else:
        print ("The word needs to be between 2-8 letters long")
        break
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
    print(Hangman[0])
    attempts = len(Hangman) - 1      
    correct_letters = []
    incorrect_guess = 0
    correct_guess = 0  #Sets up for the varibles 
    print(wordLength * "_ ")
    guess = input("Guess a letter :")
    while newwword != neword:
        allguesses = correct_guess + incorrect_guess
        if guess == firstWord or guess == secondWord or guess == thirdWord or guess == fourthWord or guess == fithWord or guess == sixthWord or guess == seventhWord or guess == eighthWord:
            correct_guess += 1
            print(Hangman[(len(Hangman) - 0) - attempts])
            if guess == firstWord:  #if the players 2 guess equals the first word and then it selects the frist letter in the list and replaces it with guess insted of "_". 
                newwword[0] = guess
            if guess == secondWord:
                newwword[1] = guess
            if guess == thirdWord:  #it uses if staitments so that there are two if the same letter it diesnt have to be guesses twice
                newwword[2] = guess
            if guess == fourthWord:
                newwword[3] = guess
            if guess == fithWord:
                newwword[4] = guess
            if guess == sixthWord:
                newwword[5] = guess
            if guess == seventhWord:
                newwword[6] = guess
            if guess == eighthWord:
                newwword[7] = guess
            print(" \n " * 3)  #adds new blank lines
            print(', '.join(newwword))  #puts the sting togeather
            print("Incorect guess, you have ", incorrect_guess, "incorrect guesses")
            print(" \n " * 2)
            if newwword == neword:
                break    
            elif correct_letters != word:
                guess = input("Have another guess: ")
                pass
            if incorrect_guess == 10:
                print("You have reached the maximum incorrect guesses:", incorrect_guess)
                print("Unlucky press y below to have another game")
                break
        else:
            incorrect_guess += 1
            print("Incorect guess, you have ", incorrect_guess, "incorrect guesses")
            if incorrect_guess == 10:
                break
            attempts -= 1
            print(Hangman[(len(Hangman) - 1) - attempts])
            print(', '.join(newwword))
            print(" \n")

            if correct_guess == wordLength:
                print("Well done, you guessed the word")
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
    if answer == 'y':  # add player swap
        print(" \n " * 10)
        print("now player 1 is player 2 and player 2 is now player 1")
        continue
    else:
        print('Goodbye')
        break
