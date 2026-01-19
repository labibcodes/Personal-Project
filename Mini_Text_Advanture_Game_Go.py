print("-----Welcome to Mini Text Advanture Game-----")
print("\nFollow the instructions to play this game! \n\n(YOU ONLY HAVE 2 CHANCES TO TRY) \nEnjoy the game!")

attempt = 0
room = "library"
has_key = False

while attempt < 3:
    #===LIBRARY===
    if room == "library":
        print("\nNow, you are in the Great Library! \nThis library has only one door that will lead you to the next room.")

        #Find the key
        if not has_key:
            Guess = input("Guess where is the key? (table, book, bottle, chair): ").lower()

            if Guess == "table":
                print("Yes, You found the key!")
                has_key = True

            else:
                attempt += 1
                print(f"Wrong choice! Attempts left: {3 - attempt}")

        #Got the key
        else:
            Option = input("\nYou got the key! what do yo do? (go north / stay): ").lower()

            if Option == "go north":
                room = "corridor"

            elif Option == "stay":
                attempt += 1
                print(f"You decided to stay! \nCome on! Attempts left: {3 - attempt}")

            else:
                print("Invalid option! Try again!")

    #===CORRIDOR===
    elif room == "corridor":
        print("\nNow, you are in the corridor! If you want to win this game, you must find the key that will lead "
              "you to finish this game!")
        Guess1 = input("Guess where is the key? (table, lamp, bottle, chair): ").lower()

        if Guess1 == "bottle":
            print("Yes, you guessed the correct choice!")
            print("\n\ncongratulations, you win!")
            break

        else:
            attempt += 1
            print(f"Wrong choice! Attempts left: {3 - attempt}")

#===GAME OVER===
if attempt == 3:
    print("\nGame over!")
