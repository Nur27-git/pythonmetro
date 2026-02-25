#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein
#Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
#Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
import random
arvaus=random.randint(1,10)
arvattu=int(input("Arvaa numero 1-10:"))
while arvattu!=arvaus:
    if arvaus>arvattu:
        print("Suurempi")
    else:
        print("Pienempi")
    arvattu=int(input("Arvaa uudestaan:"))
print("Oikein")