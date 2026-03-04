from math import sqrt

luku=int(input("Luku:"))
while luku!=0:
    if luku<0:
        print("Virheellinen luku")
    else:
        print(sqrt(luku))
    luku = int(input("Luku:"))