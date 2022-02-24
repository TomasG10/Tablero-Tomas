from Ficha import *

class Tablero:


    lista_jugadores = []

    casillas = 0


    def __init__(self):

        jug1 = Ficha('azul')
        jug2 = Ficha('verde')
        jug3 = Ficha('rodasito')

        self.lista_jugadores = [jug1,jug2,jug3]
        self.casillas = 18


    def juego(self):

        victoria = False

        while not victoria:

            for i in range(len(self.lista_jugadores)):
                self.lista_jugadores[i].avanzar()
                if self.lista_jugadores[i].posicion >= self.casillas:
                    print('El jugador' + ' ' + self.lista_jugadores[i].color + ' ' + 'ganó')
                    victoria = True
                    break

#Esta es la llamada para el main en una futura clase
tablero = Tablero()

tablero.juego()

