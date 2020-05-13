class ReverseString():
    def __init__(self, string):
        self.string = string

    def GUI(self):
        self.string = input("Please enter a string:\n")

    def reverse(self, given_string):
        return given_string[::-1]

    def play_again(self):
        pass

    def main(self):
        if self.string == "":
            self.GUI()

        reversed_string = self.reverse(self.string)
        print(f"Your given string reversed looks like this: \n{reversed_string}")

reverser = ReverseString("Hallo")
reverser.main()

reverser02 = ReverseString("")
reverser02.main()
