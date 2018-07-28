from hangmanDisplay import Hangman  #Inputs a very long varible.
while True:
    incorrect_guess = 0
    correct_guess = 0
    word = ()  #Empties the varible for multiple games
    wordLength = 8  #Set up for the while loop.
    print("\t", "Welcome to two player hangman hang man")
    word = input("Player one please enter a word for player two to guess word, no longer than 7 letters: ")
    neword = [word[x:x+1] for x in range(0,len(word),1)]  #used to separte the word so that each letter can be assigned a name.
    print(neword)
    wordLength = len(neword)  #Works out the lenth of the word.
    print((" \n") * 42)  #Seperates the player 1 part with the player 2 part.
    i = 0
    print(Hangman[0])
    attempts = len(Hangman) - 1
    print(wordLength * "_ ")
    guess = input("Guess a letter :")
    while
    for x in (0, wordLength):
        if guess = neword[i]:
            wordDisplay += guess
            print(Hangman[(len(Hangman) - 0) - attempts])
        if incorrect_guess == 10:
            print("Unlucly, you've reached the max ammount of wrong guesses")
            break
        print(" \n " * 3)  #Adds new blank lines.
        print(wordDisplay)  #Puts the sting togeather.
        print("You have ", incorrect_guess, "incorrect guesses")
        print(" \n " * 2)
        if wordDisplay == neword:  #If the word is guessed it ends while loop
                print("Well done")
                break
            elif wordDisplay != word:
                guess = input("Have another guess: ")
                pass
            if incorrect_guess == 10:
                print("You have reached the maximum incorrect guesses:", incorrect_guess)
                break
        else:
            incorrect_guess += 1
            print("Incorect guess, you have", incorrect_guess, "incorrect guesses")
            if incorrect_guess == 10:
            	print("Unlucly, you've reached the max ammount of wrong guesses")
            	break
            attempts -= 1
            print(Hangman[(len(Hangman) - 1) - attempts])
            print(', '.join(wordDisplay), " \n")  #prints the list without the separation.
            if correct_guess == wordLength:
                print("Well done, you guessed the worddd")
                print(Hangman[(len(Hangman) - 0) - attempts])
                break
            elif wordDisplay != word:
                guess = input("Have another guess: ")
    print(" \n ")
    print("The word was: ", word)
    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':  #Add player swap.
        print(" \n " * 10)
        print("Now player one is player two and player two is now player one", " \n")
        continue
    else:
        print('Goodbye')
        break
