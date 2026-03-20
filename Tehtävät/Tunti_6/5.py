def parilliset_lista(alkulista):
    parilliset=[]
    for luku in alkulista:
        if luku%2==0:
            parilliset.append(luku)
    return parilliset
def main():
    alkulista=[23,32,12,43,32,6,7,54]
    parittomat=parilliset_lista(alkulista)
    print(*alkulista)
    print(*parittomat)
main()