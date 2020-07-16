from Live import load_game, welcome
print(welcome("gadi"))
try:
    load_game()

except ValueError: print("please enter just numbers.")