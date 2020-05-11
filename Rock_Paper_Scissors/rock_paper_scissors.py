import random

choices = ["rock", "paper", "scissors"]

player_input = input("Choose your fighter:\n(1)Rock\n(2)Paper\n(3)Scissors\n")
player_choice = choices[int(player_input) - 1]
ai_choice = choices[random.randint(0, 2)]

print("\n", player_choice, " - ", ai_choice)
