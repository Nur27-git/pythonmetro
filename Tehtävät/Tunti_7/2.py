nimet=set()
nimi=input("Anna nimi, tyhjä lopettaa:")
while nimi!="":
    if nimi in nimet:
        print("Aiemmin syötetty")
    else:nimet.add(nimi)
    print("Uusi nimi")
    nimi = input("Anna nimi, tyhjä lopettaa:")
print("Nimilista")
for nimi in nimet:
    print(nimi)