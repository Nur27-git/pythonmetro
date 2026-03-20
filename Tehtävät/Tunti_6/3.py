def gallona_litra(gallon):
    return gallon*3.785


def main():
    while True:
        gallon= float(input("Anna gallon määrä:"))

        if gallon<0:
            break
        litrat=gallona_litra(gallon)
        print(f" Antamasi määrä on {litrat} litraa")
main()


