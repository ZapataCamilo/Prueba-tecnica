import sys

def palindromo():
    p = sys.argv[1].lower()
    for i in range(0, int(len(p)/2)):
        if p[i] != p[-i-1]:
            print(False)
        else:
            print(True)

palindromo()