import time, sys, os
import random
from colorama import init
from termcolor import colored

init()
clear = lambda: os.system('cls')

answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes - definitly", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
            "Yes", "signs point to yes", 
            "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
            "Dont count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]


def magic_8_ball():
    clear()
    question = input("Please enter a question:\n")
    print(colored("Thinking...", "blue"))
    time.sleep(2)
    answer = random.randint(0, len(answers))
    print(answers[answer])

    again = input("Ask another question? (y/n)")
    if again == "y":
        magic_8_ball()
    elif again == "n":
        sys.exit()

if __name__ == "__main__":
    magic_8_ball()
