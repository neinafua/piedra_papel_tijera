from random import *
# entrada
jugador = (input("escoja: piedra, papel o tijera:"))

#proceso
opciones = ["piedra", "papel", "tijera"]
computadora = choice(opciones)
if jugador == computadora:
    print("ambos escogieron", (computadora), "por lo tanto es un empate")
elif(jugador == "piedra" and computadora == "tijeras") or \
    (jugador == "papel" and computadora == "piedra") or \
    (jugador == "tijeras" and computadora == "papel"):
        print("el compuatdor escogio", (computadora), "por lo tanto gano")
else:
    print("el compuatdor escogio", (computadora), "por lo tanto perdio")