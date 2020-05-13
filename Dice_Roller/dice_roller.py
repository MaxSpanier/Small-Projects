import random, sys

def roll():
    number = random.randint(1, 6)
    print(f"You rolled a {number}")
    again = input("Roll again? y/n\n")
    print("-----------------------")
    if again == "y":
        roll()
    else:
        sys.exit()

if __name__ == "__main__":
    print("-----------------------")
    roll()
