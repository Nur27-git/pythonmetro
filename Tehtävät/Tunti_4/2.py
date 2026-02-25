#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
tuuma = float(input("Anna tuumat:"))
while tuuma>=0:
    print(f"{tuuma} tuumaa on {tuuma*2.54} cm")
    tuuma=int(input("Anna tuumat:"))
else: print("Luku on negatiivinen")
