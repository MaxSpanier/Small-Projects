'''
Prints out the lyrics to the song "99 bottles of beer on the wall" without typing everything in manually
'''

i = 99

while i != 0:
    if i > 1:
        print(i, "bottles of beer on the wall, ", i, " bottles of beer.\nTake one down and pass it around, ", i-1 ," bottles of beer on the wall.")
        i = i-1
    elif i == 1:
        print(i, "bottle of beer on the wall, ", i, " bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.")
        i = i-1
    elif i == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
        i = i-1
