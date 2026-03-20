import random
def randomi(tahkot):
    return random.randint(1,tahkot)

def main():
    tahkot= int(input("Anna tahkot: "))
    luku=0
    while luku !=tahkot:
        luku = randomi(tahkot)
        print(luku)

main()
