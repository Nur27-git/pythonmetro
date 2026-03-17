#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

jono = []
luku = input("Anna luku: ")

while luku != "":
    jono.append(int(luku))
    luku = input("Anna luku: ")
jono.sort(reverse=True)
print("Viisi suurinta", *jono[:5])
