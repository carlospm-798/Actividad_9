"""
Carlos Paredes Márquez.
Funciones de particulas.
26/10/2020.
"""
from particula import Particula

#Administrador de funciones.

class Particulas:
    def __init__(self):
        self.__parti = []
    
    def agregar_inicio(self, particula:Particula):
        self.__parti.insert(0, particula)
    
    def agregar_final(self, particula:Particula):
        self.__parti.append(particula)
    
    def mostrar(self):
        for particula in self.__parti:
            print(particula)

p01 = Particula(id="16", origen_x="0", origen_y="2", destino_x="7", destino_y="14", velocidad="180", red="18", green="21", blue="14", distancia="")
p02 = Particula("17", "1", "3", "18", "54", "210", "2", "4", "6", "")

particulas = Particulas()
particulas.agregar_inicio(p01)
particulas.agregar_final(p02)
particulas.agregar_inicio(p01)
particulas.mostrar()