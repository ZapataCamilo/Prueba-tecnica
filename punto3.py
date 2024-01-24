import sys

def fizzbuzz():
    fz = sys.argv[1]
    p = int(fz)

    if p % 3 == 0 and p % 5 == 0:
        print('FizzBuzz')
        
    elif p % 3 == 0:
        print('Fizz')

    elif p % 5 == 0:
        print('Buzz')

fizzbuzz()