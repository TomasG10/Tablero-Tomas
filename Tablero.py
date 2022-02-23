from Ficha import *

class Tablero:

    #Defina aquí los atributos de Tablero
    jugadores = []

    def __init__(self):

        jug1 = Ficha('verde')
        jug2 = Ficha('azul')

        self.jugadores = [jug1,jug2]
    

    def mover_jugadores(self):

        cont = 0
        while cont <= 16:
            for i in self.jugadores:
                i.avanzar()
                if i.posicion >= 20:
                    print(i.color)
                    break
            cont += 1


