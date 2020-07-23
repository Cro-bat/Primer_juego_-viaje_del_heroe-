import random
import Dialogos


def roll_dice(num):
    return random.randint(1, num)


def interactuar(evento, puntuacion, hp, derrota):
    derrota = False
    dado = roll_dice(6)

    if dado > evento.probabilidad:
        hp += evento.castigo
        print(evento.descripcion_castigo)
    else:
        if evento.premio_es_atajo:
            puntuacion += 1
            print(evento.descripcion_premio)
        else:
            hp += evento.premio
            print(evento.descripcion_premio)

    if hp > 0:
        puntuacion += 1

    else:
        derrota = True

    print("HP =", hp)
    print("Recorrido =", puntuacion)

    return hp, puntuacion, derrota


def comprobar_victoria(derrota,puntuacion):
    if derrota == False:
        print(Dialogos.victoria[0], puntuacion)
    else:
        print(Dialogos.victoria[1], puntuacion)
