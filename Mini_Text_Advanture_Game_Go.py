print("Welcome to Mini Text Advanture Game")
print("Follow the instructions to play this game! Enjoy the game!")

while True:
    #Library
    print("Now, you are in the Great Library! This library has only one door that will lead you to the next room.")
    Guess = input("Guess where is the key? (table, book, bottle, chair) ")
    if Guess == "table":
        print("Yes, You guessed the correct choice!")
        Option = input("You got the key! what do yo do? (Go north, stay in this library) ")
        if Option == "Go north":
            #Corridor
            print("Now, you are in the corridor! If you want to win this game, you must find the key that will lead "
                  "you to finish this game!")
            Guess1 = input("Guess where is the key? (table, lamp, bottle, chair) ")
            if Guess1 == "bottle":
                print("Yes, you guessed the correct choice!")
                print("congratulations, you win!")
                break

            elif Guess1 == "lamp":
                print("Oh no, you guessed the wrong choice!")
                print("Thanks for playing!")
                break

            elif Guess1 == "chair":
                print("Oh no, you guessed the wrong choice!")
                print("Thanks for playing!")
                break

            elif Guess1 == "table":
                print("Oh no, you guessed the wrong choice!")
                print("Thanks for playing!")
                break

            else:
                print("Sorry, that's not a valid choice! You lose")
                print("Thanks for playing!")
                break

        elif Option == "stay in this library":
            print("Oh no, why? So you doesn't want to continue this game!")
            print("Okay then, Thanks for playing!")
            break
    elif Guess == "book":
        print("Oh no, you guessed the wrong choice!")
        print("Thanks for playing!")
        break

    elif Guess == "bottle":
        print("Oh no, you guessed the wrong choice!")
        print("Thanks for playing!")
        break

    elif Guess == "chair":
        print("Oh no, you guessed the wrong choice!")
        print("Thanks for playing!")
        break

    else:
        print("Sorry, that's not a valid choice! You lose")
        print("Thanks for playing!")
        break