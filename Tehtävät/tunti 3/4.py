vuosi=int(input("Vuosi:"))

if (vuosi % 400 == 0) or (vuosi % 4 == 0 and vuosi % 100 != 0):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")

luku1=int(input("Luku:"))
if luku1 <0:
    print(f"Luvun itseisarvo {(luku1*-1)}")
else:
    print(f"Luvun itseisarvo {luku1}")