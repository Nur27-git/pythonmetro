import random
def randomi():
    return random.randint(1,6)

def main():
    luku=0
    while luku !=6:
        luku = randomi()
        print(luku)

main()
