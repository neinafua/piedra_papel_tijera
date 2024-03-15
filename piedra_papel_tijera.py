import random

def piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]

    print("¡Bienvenido a Piedra, Papel, Tijeras!")
    while True:
        jugador = input("Elige piedra, papel o tijeras (o 'q' para salir): ").lower()
        if jugador == 'q':
            break
        elif jugador not in opciones:
            print("Opción inválida. Inténtalo de nuevo.")
            continue

        computadora = random.choice(opciones)
        print(f"La computadora eligió {computadora}.")

        if jugador == computadora:
            print("¡Empate!")
        elif (jugador == "piedra" and computadora == "tijeras") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijeras" and computadora == "papel"):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")

piedra_papel_tijeras()
