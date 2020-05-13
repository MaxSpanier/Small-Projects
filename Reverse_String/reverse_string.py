import sys

class ReverseString():
    def __init__(self, string):
        self.string = string

    def GUI(self):
        self.string = input("Please enter a string:\n")

    def reverse(self, given_string):
        return given_string[::-1]

    def play_again(self):
        choice = str(input("-------------------------------\nDo you want to reverse another string? (y/n) - "))
        if choice == "y":
            self.string = ""
            self.main()
        elif choice == "n":
            sys.exit()
        else:
            print("Plese enter a valid answer.")
            self.play_again()

    def main(self):
        if self.string == "":
            self.GUI()

        reversed_string = self.reverse(self.string)
        print(f"Your given string reversed looks like this: \n{reversed_string}")

        self.play_again()

# reverser = ReverseString("Hallo")
# reverser.main()

reverser02 = ReverseString("")
reverser02.main()
