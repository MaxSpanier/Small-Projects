'''
A function that checks wheter the input is a narcisstic number or not
A number is called narcisstic number if a number is the sum of ots own digits each raised to the power of the number of digits
'''

def is_narcisstic_number(number):
    sum = 0
    if len(str(number)) == 1:
        print(number, "is a narcisstic number")
    else:
        n = len(str(number))
        digits = [int(x) for x in str(number)]
        for d in range(n):
            sum += pow(digits[d], n)
        if sum == number:
            print(number, "is a narcisstic number")
        else:
            print(number, "is NOT a narcisstic number")

is_narcisstic_number(21897142587612075)
is_narcisstic_number(63105425988599693916)
is_narcisstic_number(24678050)
