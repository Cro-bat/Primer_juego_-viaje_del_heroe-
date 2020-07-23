# -*- coding: utf-8 -*-
from Clases import Lugar
from Clases import Evento

import Dialogos
import Funciones

puntuacion_necesaria = 10
hp_inicial = 5


eventos = [
    Evento("dormir", 2, False, -3, 4, Dialogos.descripciones_eventos[0], Dialogos.descripciones_triunfos[0],
           Dialogos.descripciones_castigos[0]),
    Evento("cazar", 1, False, -2, 3, Dialogos.descripciones_eventos[1], Dialogos.descripciones_triunfos[1],
           Dialogos.descripciones_castigos[1]),
    Evento("comer", 2, False, 1, 1, Dialogos.descripciones_eventos[2], Dialogos.descripciones_triunfos[2],
           Dialogos.descripciones_castigos[2]),
    Evento("hablar", 0, True, -3, 2, Dialogos.descripciones_eventos[3], Dialogos.descripciones_triunfos[3],
           Dialogos.descripciones_castigos[3]),
    Evento("escalar", 0, True, -4, 3, Dialogos.descripciones_eventos[4], Dialogos.descripciones_triunfos[4],
           Dialogos.descripciones_castigos[4]),
    Evento("rodear", 0, False, -1, 3, Dialogos.descripciones_eventos[5], Dialogos.descripciones_triunfos[5],
           Dialogos.descripciones_castigos[5]),
    Evento("pescar", 2, False, -4, 2, Dialogos.descripciones_eventos[6], Dialogos.descripciones_triunfos[6],
           Dialogos.descripciones_castigos[6]),
    Evento("contar chiste", 0, True, 0, 6, Dialogos.descripciones_eventos[7], Dialogos.descripciones_triunfos[7],
           Dialogos.descripciones_castigos[7]),
    Evento("comprar", 3, False, 0, 6, Dialogos.descripciones_eventos[8], Dialogos.descripciones_triunfos[8],
           Dialogos.descripciones_castigos[8])
]

dormir = eventos[0]
cazar = eventos[1]
comer = eventos[2]
hablar = eventos[3]
escalar = eventos[4]
rodear = eventos[5]
pescar = eventos[6]
contar_chiste = eventos[7]
comprar = eventos[8]

lugares = [
    Lugar(1, 20, Dialogos.descripciones_lugares[0], dormir, cazar),
    Lugar(21, 40, Dialogos.descripciones_lugares[1], comer, hablar),
    Lugar(41, 75, Dialogos.descripciones_lugares[2], escalar, rodear),
    Lugar(76, 90, Dialogos.descripciones_lugares[3], dormir, pescar),
    Lugar(91, 100, Dialogos.descripciones_lugares[4], contar_chiste, comprar)
]

bosque = lugares[0]
ciudad = lugares[1]
montana = lugares[2]
lago = lugares[3]
viajero = lugares[4]

print(Dialogos.saludo[0])
nombre = input(Dialogos.saludo[1])
edad = int(input(Dialogos.saludo[2]))

print("\nHola", nombre, "tienes,", edad, "años.")

if edad >= 18:
    print("¡Tienes edad suficiente para jugar!")
    quiere_jugar = input("¿Quieres jugar? ").lower()

    if quiere_jugar == "si" or "yes" or "y" or "s":
        puede_jugar = True
        print("\n¡Comienza la aventura! (HP = 5)\n")

    else:
        puede_jugar = False
        print("Adiós...")

elif edad >= 13:
    print("¡Puedes jugar bajo supervisión!")
    quiere_jugar = input("¿Quieres jugar? ").lower()

    if quiere_jugar == "si":
        puede_jugar = True
        print("\n¡Comienza la aventura!\n")
    else:
        puede_jugar = False
        print("Adiós...")

else:
    puede_jugar = False
    print("¡Eres muy joven para jugar!")
    print("Adiós...")

while puede_jugar:
    puntuacion = 0
    hp = hp_inicial
    derrota = False

    while puntuacion < puntuacion_necesaria and derrota == False:
        dado = Funciones.roll_dice(100)
        if dado <= 20:
            lugar_actual = bosque
        elif dado <= 35:
            lugar_actual = ciudad
        elif dado <= 65:
            lugar_actual = montana
        elif dado <= 95:
            lugar_actual = lago
        else:
            lugar_actual = viajero

        print(lugar_actual.descripcion)
        print("a)", lugar_actual.evento_1.nombre, "b)", lugar_actual.evento_2.nombre)
        decision = ""

        while decision != "a" and decision != "b":
            decision = input()

            if decision != "a" and decision != "b":
                print("Esa opción no existe.")

        if decision == "a":
            evento_actual = lugar_actual.evento_1
        else:
            evento_actual = lugar_actual.evento_2

        print(evento_actual.descripcion)

        (hp, puntuacion, derrota) = Funciones.interactuar(evento_actual, puntuacion, hp, derrota)
        print("\n")

    Funciones.comprobar_victoria(derrota, puntuacion)

    quiere_jugar = input("\n¿Reintentar? ").lower()
    print("\n")
    if quiere_jugar != "si" and "yes" and "y" and "s":
        puede_jugar = False