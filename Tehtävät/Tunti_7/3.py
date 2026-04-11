lentoasemat={}
while True:
    print("1. Lisää lentoasema, 2. Hae asemaa, 3. Lopeta")
    valinta=int(input("valintasi:"))
    if valinta==1:
        icao=input("Anna icao:")
        nimi=input("Anna nimi:")
        lentoasemat[icao]=nimi
        print("Lentoasema", lentoasemat[icao], "tallennettu")

    elif valinta ==2:
        icao=input("Haettavan icao:")
        if icao in lentoasemat:
            print(f"{icao}: {lentoasemat[icao]}")
        else:
            print("Lentoasema ei löydy")
    elif valinta ==3:
        print("Loppu")
        break
    else:
        print("Virheellinen valinta")


