from tokenize import endpats

nimi=input("nimi:")
if nimi=="Matti":
    print("Seuraava, kiitos")
else:
    maara=int(input("Montako keittoannosta?"))
    hinta=maara*5.9
    print("Kokonaishinta on", hinta)
    print("Seuraava, kiitos")