
import random

compu = random.randrange(1,4)

Pipo = input("elegi flaco: Piedra, Papel o Tijeras: ")

if compu == 1:
    print("la pc eligió Piedra")
elif compu == 2:
    print("la pc eligió Papel")
else:
    print("la pc eligió Tijeras")

if (Pipo == "Piedra" and compu == 1) or (Pipo == "Papel" and compu == 2) or (Pipo == "Tijeras" and compu == 3):
    print("empataban era durisimo")
elif (Pipo == "Piedra" and compu == 2) or (Pipo == "Papel" and compu == 3) or (Pipo == "Tijeras" and compu == 1):
    print("gano la pc jijij")
if (Pipo == "Piedra" and compu == 3) or (Pipo == "Papel" and compu == 1) or (Pipo == "Tijeras" and compu == 2):
    print("gano pipo")