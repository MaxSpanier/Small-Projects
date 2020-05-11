def reverse():
    print("This programm will reverse the given string")
    string = input("Please enter a string: ")

    reversed = string[::-1]
    
    return reversed

if __name__ == "__main__":
    print(reverse())
