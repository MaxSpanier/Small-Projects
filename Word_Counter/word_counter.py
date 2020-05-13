def word_counter():
    string = input("Please enter a sentence: ")
    words = string.split(" ")
    counter = len(words)
    return f"The given sentence has {counter} words in it"

if __name__ == "__main__":
    print(word_counter())
