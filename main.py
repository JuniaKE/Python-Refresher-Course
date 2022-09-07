def get_choices():
  player_choice = input("Enter a Choice(rock, paper, scissors)")                                                                                                                                 
  computer_choice = input("Enyer a Computer Choice")
  choices = { "player" : player_choice, "computer" : computer_choice}
  return choices

def greeting():
  return "Hi"

choice = get_choices()
print(choice)

# Gets the greeting then prints it out
response = greeting()
print(response)


dict = {"name": "Brian", "color": choice}