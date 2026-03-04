tarina = []
edellinen = ""
sana = input("Anna sana lisättäväksi tarinaan: ")

while sana != "loppu" and sana != edellinen:
    tarina.append(sana)
    edellinen = sana
    sana = input("Anna sana lisättäväksi tarinaan: ")

print(" ".join(tarina))