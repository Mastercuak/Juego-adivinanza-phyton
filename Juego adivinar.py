

import random

numerosecreto = random.randint(1,101)
intentos = 0
limite = 5
Puntos = 0

print("¡AMIGO ESTOY HACIENDO UN RE VIRUS!")

while intentos <= limite:
    if intentos == limite and Puntos == 0:
        print("flaco sos muy malo fuera de joda", """
El numero era""", numerosecreto)
        break
    elif intentos == limite and Puntos == 1:
        print("bue, adivinaste ", Puntos, " sola vez. Tampoco te creas...", """
El numero era""", numerosecreto)
        break
    elif intentos == limite and Puntos == 2:
        print("adivinaste ", Puntos, " veces. Cualquiera con un poco de suerte puede...", """
El numero era""", numerosecreto)
        break
    elif intentos == limite and Puntos == 3:
        print(Puntos, " veces seguidas. Bravo...", """
El numero era""", numerosecreto)
        break
    elif intentos == limite and Puntos > 3:
        print("bien ahi adivinaste ", Puntos, " veces seguidas. Conseguite una vida...", """
El numero era""", numerosecreto)
        break
    numero = int(input("""introduci un numero del 1 al 100:
"""))

    if numero == numerosecreto:
        print("no hay chance de que le hayas pegado")
        Puntos += 1
        numerosecreto = random.randint(1,101)
        intentos = -1
    elif numero < numerosecreto and intentos < limite - 1:
        print("es mas grande que eso capo")
    elif numero > numerosecreto and intentos < limite - 1:
        print("para chabon es un monton eso")
    intentos += 1