while True:
    first_word = () 
    second_word = ()
    third_word = ()
    fourth_word = ()
    fith_word = ()
    sixth_word = ()
    seventh_word = ()
    eighth_word =()
    chances = int(0)
    print("\t welcome to two player hangman hang man", "\t ")
    word = input("player one enter a word for player two to guess word : ")  # add range
    chances = int(input("how many errors can player 2 make? 10 to 150: "))
    while chances < 9 and chances > 151:
        if chances < 10:
            chances = int(input("please enter a number higher than 10 and lower than 150: "))
            print("nooo")
        elif chances > 151:
            chances = int(input("please enter a number lower than 150 but than 10: "))
            print("no")
        else:
            print(chances)
            print("noo")
        
    lenth = len(word)
    underscore = lenth * "__  "
    list_word = list(word)
    print((" \n") * 40)
    print("\t", underscore)
    print((" \n") * 2)
    
    if lenth == 2:
        first_word, second_word = word
        lenth_number = 2
    elif lenth == 3:
        first_word, second_word, third_word = word
        lenth_number = 3
    elif lenth == 4:
        first_word, second_word, third_word, fourth_word = word
        lenth_number = 4
    elif lenth == 5:
        first_word, second_word, third_word, fourth_word, fith_word = word
        lenth_number = 5
    elif lenth == 6:
        first_word, second_word, third_word, fourth_word, fith_word, sixth_word = word
        lenth_number = 6
    elif lenth == 7:
        first_word, second_word, third_word, fourth_word, fith_word, sixth_word, seventh_word = word
        lenth_number = 7
    elif lenth == 8:
        first_word, second_word, third_word, fourth_word, fith_word, sixth_word, seventh_word, eighth_word = word
        lenth_number = 8
    else:
        print ("the word needs to be betwween 2-8 letters long")
    correct_letters = 0
    incorrect_guess = (0)    
    #print(lenth_number)   # get rid of this
    guess = input("guess a letter :")
    letter correct = 2
    while correct_letters != lenth_number:  # or incorrect_guess == chances
        if guess == first_word or guess == second_word or guess == third_word or guess == fourth_word or guess == fith_word or guess == sixth_word or guess == seventh_word or guess == eighth_word:
            print("you have guessed a correct letter")
            correct_letters += 1
            print("you have ", correct_letters,"correct letters and guessed", incorrect_guess,"letters wrong")
        else:
            incorrect_guess += 1
            print("another incorect guess", incorrect_guess, "you have ", correct_letters,"correct letters")
            print(" \n")
            if incorrect_guess == chances:
                print("you have reached the maximum incorrect guesses:", incorrect_guess)
                break
        if correct_letters != lenth_number:
            guess = input("take another guess:")
    print(" \n ")
    print("the word was:", word)
    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':  # add player swap
        continue
    else:
        print('See you later')
        break
