def guessing_number ():
    import random
    global totalScore
    print ("This program is for guessing the number")
    guess1 = int(input("Enter lesser value number: "))
    guess2 = int(input("Enter more value number: "))
    round = int(input("Enter round: "))

    number = random.randint (guess1, guess2)

    for i in range (round):
        ans = int(input("Enter your guessing number: "))

        if ans == number:
            print ("Correct! You are a god!")
        elif ans != number:
            print ("Wrong!")
        else:
            print ("Error!")

    continue_choice = input("Do you want to continue (y/n)\n")
    if continue_choice == "y":
        guessing_number ()
    elif continue_choice == "n":
        print ("Good Bye!")
    else:
        print ("Error!")

guessing_number ()