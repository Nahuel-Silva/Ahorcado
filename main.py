from Ahorcado import Ahorcado
from AhorcadoService import AhorcadoService


class Menu():
    def opciones_jugadores(self):
        print("\n\n =======> El juego acaba de comenzar <======= \n")
        print("1 =======>  1 Jugador <======= \n")
        print("2 =======>  2 Jugadores <======= \n")
        print("3 =======>  ¿Ver resultados? <======= \n")
        print("4 =======>  Salir <======= \n")
        return int(input("Elija una opcion: "))


if __name__ == "__main__":

    while True:
        jugadores = Menu().opciones_jugadores()
        if jugadores == 1:
            unJugador = Ahorcado()
            unJugador.un_jugador()
        if jugadores == 2:
            dosJugadores = Ahorcado()
            dosJugadores.dos_jugadores()
        if jugadores == 3:
            resultado = AhorcadoService()
            resultado.ver_partida_guardada()
        if jugadores == 4:
            print("\n¡Chau vuelvas prontos!\n")
            break
