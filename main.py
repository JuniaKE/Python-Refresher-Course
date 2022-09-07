import random

def get_choices():
  player_choice = input("Enter a Choice(rock, paper, scissors)") 
  options = ["rocks","paper","scissors"]                                                                                                                                
  computer_choice = random.choice(options)
  choices = { "player" : player_choice, "computer" : computer_choice}
  return choices

choice = get_choices()
print(choice)

food = ["pizza", "carrots", "eggs"]

dinner = random.choice(food)

print(dinner)