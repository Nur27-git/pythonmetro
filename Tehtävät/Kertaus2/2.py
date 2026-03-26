jono=[]
arvo=int(input("Anna arvo, nolla lopettaa:"))
while arvo!=0:
    jono.append(arvo)
    print("Lista nyt", *jono)
    print("Lista järjestyksessä", *sorted(jono))
    arvo = int(input("Anna arvo, nolla lopettaa:"))
