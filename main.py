# Imported Random module
import random
# Printed Welcome message as well as a space
print("Welcome To The Dice Roll Game!")
print("\n")
# While loop... While true print instructions for game, then outlined the control form/requirements for game to work as expected as well as how to end game
while True:
  print(''' Enter "Play" to Play Game Or "Stop" to Stop Game ''')
  user = str(input("What would you like to do \n"))
  if user == ("Play"):
    number = random.randint(1,10)
    print("The number that was rolled was: ")
    print(number)
  elif user == "Stop":
    print("Thanks for playing :)")
    break
