def summarum (lista):
    summa=0
    for luku in lista:
        summa += luku
    return summa
def main():
    lista=[1,2,3,4,5,45324,5,42,]
    tulos=summarum(lista)
    print("Summa on", tulos)
main()
