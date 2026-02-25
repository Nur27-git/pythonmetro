#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).
k_tun=input("Käyttäjätunnus:")
ssana=input("Salasana:")
yritykset=1
while k_tun!="python" and ssana!="rules" and yritykset<5:
    print("Väärin, yritä uudestaan")
    k_tun = input("Käyttäjätunnus:")
    ssana = input("Salasana:")
    yritykset += 1

if k_tun=="python" and ssana=="rules":
    print("Tervetuloa")
else:
    print("Pääsy evätty")
