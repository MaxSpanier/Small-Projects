def check_palindrom():
    print("This programm will check if the given string is a palindrom")
    string = input("Please enter a string: ")

    string_reverse = string[::-1]

    if(string.lower() == string_reverse.lower()):
        return f"The given word {string} is a palindrom" 
    else:
        return f"The given word {string} is NOT a palindrom" 

if __name__ == "__main__":
    print(check_palindrom())
