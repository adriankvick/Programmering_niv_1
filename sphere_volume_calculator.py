import math
Sfär_radie=int(input("Sfärens radie:"))

Sfär_volym=float((4/3)*math.pi*(Sfär_radie**3))
Sfär_area=float(4*math.pi*(Sfär_radie**2))

print(f"Sfärens volym:{round(Sfär_volym,3)}")
print(f"Sfärens area:{round(Sfär_area,3)}")