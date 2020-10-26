from ServicePartidas import ServicesPartidas
from AhorcadoService import AhorcadoService


class Ahorcado():
    def un_jugador(self):
        nombre_jugador = input("\nNombre del jugador/a: ")
        dificultad = int(input("\nLa dificultad de su partida es (1 al 10): "))
        partida = ServicesPartidas().\
            iniciar_partida(nombre_jugador, dificultad, "", "")
        termino = False
        while not termino:
            print("\nEl tipo de palabra es: ", partida.tipo_palabra, "\n")
            print(partida.palabra_aciertos)
            letra = input("\nIngrese una letra o numero ----> ")
            if(letra == "salir"):
                print("!Gracias vuelvas prontos!")
                return True
            resultado = ServicesPartidas().\
                intentar_letra(partida, letra.upper())
            if(resultado != "Continua"):
                if(resultado == "Gano"):
                    print("\n\nGanaste eres el puto amo!\n\n")
                    print("La palabra que toco era: ", partida.palabra)
                else:
                    print(
                        "\n\n\nLo siento, la palabra era ",
                        partida.palabra, "\n\n\n"
                    )
                    print("La proxima sera")
                termino = True
        AhorcadoService().guardar_partida(partida, partida.nombre_jugador)
        return True

    def dos_jugadores(self):
        nombre_uno = input("\nNombre del jugador/a 1: ")
        dificultad = int(input(
            "\nLa dificultad de la partida de su oponente es (1 al 10): "
        ))
        palabra = input("\nIngrese la palabra para su oponente: ")
        tipo_palabra = input("\nIngrese el tipo de palabra: ")
        partida = ServicesPartidas().iniciar_partida(
            nombre_uno, dificultad, palabra, tipo_palabra)
        termino = False
        while not termino:
            print("\nEl tipo de palabra es: ", tipo_palabra, "\n")
            print(partida.palabra_aciertos)
            letra = input("\nIngrese una letra ----> ")
            if(letra == "salir"):
                print("¡Gracias por jugar vuelvas prontos!")
                return True
            result = ServicesPartidas().intentar_letra(partida, letra.upper())
            if(result != "Continua"):
                if(result == "Gano"):
                    print(
                        "\n\n¡Felicitaciones, Ganaste eres un numero uno!\n\n"
                        )
                else:
                    print(
                        "\n\n\nLo siento, la palabra era ",
                        palabra, "\n\n\n"
                    )
                    print("La proxima sera")
                termino = True
        AhorcadoService().guardar_partida(partida, partida.nombre_jugador)
        nombre_dos = input("\nNombre del jugador/a 2: ")
        dificultad = int(input(
            "\nLa dificultad de la partida de su oponente es (1 al 10): "
            ))
        palabra = input("\nIngrese la palabra para su oponente: ")
        tipo_palabra = input("\nIngrese el tipo de palabra: ")
        partida = ServicesPartidas().iniciar_partida(
            nombre_dos, dificultad, palabra, tipo_palabra)
        termino = False
        while not termino:
            print("\nEl tipo de palabra es: ", tipo_palabra, "\n")
            print(partida.palabra_aciertos)
            letra = input("\nIngrese una letra ----> ")
            if(letra == "salir"):
                print("¡Gracias por jugar vuelvas prontos!")
                return True
            result = ServicesPartidas().intentar_letra(partida, letra.upper())
            if(result != "Continua"):
                if(result == "Gano"):
                    print(
                        "\n\n¡Felicitaciones, Ganaste eres un numero uno!\n\n"
                    )
                else:
                    print(
                        "\n\n\nLo siento, la palabra era ",
                        palabra, "\n\n\n"
                    )
                    print("La proxima sera")
                termino = True
        AhorcadoService().guardar_partida(partida, partida.nombre_jugador)
        return True
