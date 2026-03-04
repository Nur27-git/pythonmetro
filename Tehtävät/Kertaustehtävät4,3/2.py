palkka=int(input("Palkka:"))
tunnit=int(input("Tunnit:"))
päivä=input("Viikonpäivä:")
if päivä=="Sunnuntai":
    paivap=tunnit*palkka*2
    print("Päiväpalkka:", paivap)
else:
    print("Päiväpalkka:", (palkka*tunnit))