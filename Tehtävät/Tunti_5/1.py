#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
import random
määrä=int(input("Anna arpakuutioiden lukumäärä:"))
summa=0
for i in range(määrä):
    summa+=random.randint(1,6)

print(f"Summa on {summa}")


