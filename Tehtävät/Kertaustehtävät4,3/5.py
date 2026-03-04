print("Valitse 1 (yhteenlasku), 2 (vähennyslasku), 3 (kertolasku), 4 (jakolasku), 0 lopettaa) ")
valinta=input("Valinta:")
while valinta!="0":
    if valinta=="1":
        a=float(input("Anna ensimmäinen luku:"))
        b=float(input("Anna toinen luku:"))
        print("Summa on", a+b)
    elif valinta=="2":
        a = float(input("Anna ensimmäinen luku:"))
        b = float(input("Anna toinen luku:"))
        print("Erotus on", a-b)
    elif valinta=="3":
        a = float(input("Anna ensimmäinen luku:"))
        b = float(input("Anna toinen luku:"))
        print("Tulo on", a*b)
    elif valinta=="4":
        a = float(input("Anna ensimmäinen luku:"))
        b = float(input("Anna toinen luku:"))
        if b==0:
            print("Ei voi laskea")
        else:
            print("Jako on", a/b)
    print("Valitse 1 (yhteenlasku), 2 (vähennyslasku), 3 (kertolasku), 4 (jakolasku), 0 lopettaa) ")
    valinta = input("Valinta:")
print("Ohjelma lopetettu")


