import random, sys

class DiceRoller():
    def __init__(self):
        pass
    
    def roll(self):
        number = random.randint(1, 6)
        return number

    def play_again(self):
        again = input("Roll again? y/n\n")
        print("-----------------------")
        if again == "y":
            self.play()
        elif again == "n":
            sys.exit()
        else:
            print("Plese enter a valid answer.")
            self.play_again()

    def play(self):
        rolled = self.roll()
        print(f"You rolled a {rolled}")
        self.play_again()

roller = DiceRoller()
roller.play()
