def suurin_arvo(eka, toka, kolmas):
    if eka >= toka and eka >= kolmas:
        return eka
    elif toka >= eka and toka >= kolmas:
        return toka
    else:
        return kolmas

eka=int(input("Anna numero:"))
toka=int(input("Anna numero:"))
kolmas=int(input("Anna numero:"))
print("Suurin arvo on", suurin_arvo(eka,toka,kolmas))