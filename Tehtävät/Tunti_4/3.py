#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
jono = []
luku = input("Anna luku: ")

while luku != "":
    jono.append(int(luku))
    luku = input("Anna luku: ")

if jono:
    print("Suurin:", max(jono))
    print("Pienin:", min(jono))
else:
    print("Et antanut yhtään lukua.")