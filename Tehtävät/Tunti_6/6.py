import math
def yksikhinta(halkaisija, hinta):
    sade = halkaisija / 100 / 2
    pinta_ala = math.pi * sade * sade
    return hinta/pinta_ala

def main():
    print("Pizza 1")
    d1=float(input("Anna pizzan 1 halkaisija:"))
    h1=float(input("Anna pizzan 1 hinta:"))
    print("Pizza 2")
    d2 = float(input("Anna pizzan 2 halkaisija:"))
    h2 = float(input("Anna pizzan 2 hinta:"))
    y1=yksikhinta(d1,h1)
    y2=yksikhinta(d2,h2)
    print(" Pizzan 1 yksikköhinta", y1)
    print(" Pizzan 2 yksikköhinta", y2)
    if y1<y2:
        print("Pizza 1 edullisempi")
    elif y1>y2:
        print("Pizza 2 edullisempi")
    else:
        print("Saman hintaisia")
main()
