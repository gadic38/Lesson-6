def welcome (name):

    print("Hello " + (name) + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")

    return

def load_game():

        print("Please choose a game to play:\n" 
        "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
        "2. Guess Game - guess a number and see if you chose like the computer.\n"
        "3. Currency Roulette - try and guess the value of a random amount of USD in ILS.")


        game_number = int(input())


        if game_number <= 3 and game_number > 0 :
                print("Please choose game difficulty from 1 to 5:")
                difficulty_level = int(input())
                if difficulty_level <= 5:
                    pass
                else:print("you choose the wrong number!!!!")
        else:print("you choose the wrong number!!!!")



