sp=input("Sukupuolesi:")
hg=int(input("Hemoglobiiniarvosi:"))
if sp=="Mies" and hg>195:
    (print("Korkea"))
elif sp=="Mies" and hg<134:
    (print("Matala"))
if sp=="Mies" and hg<=195 and hg>134:
    (print("Normaali"))
if sp == "Nainen" and hg > 175:
    (print("Korkea"))
elif sp == "Nainen" and hg < 117:
    (print("Matala"))
if sp == "Nainen" and hg<= 175 and hg > 117:
    (print("Normaali"))
