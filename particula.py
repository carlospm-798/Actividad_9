"""
Carlos Paredes Márquez.
Función 'particula'.
26/10/2020.
"""
from algoritmos import distancia_euclidiana

class Particula: #Definimos la clase particula.
    def __init__(self, id=0, origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0, red=0, green=0, blue=0, distancia=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(2, 2, 4, 4)

    def __str__(self):
        return(
            "id: " + str(self.__id) + "\n" +
            "Origen x: " + str(self.__origen_x) + "\n" +
            "Origen y: " + str(self.__origen_y) + "\n" +
            "Destino x: " + str(self.__destino_x) + "\n" +
            "Destino y: " + str(self.__destino_y) + "\n" +
            "Velocidad: " + str(self.__velocidad) + "\n" +
            "Red: " + str(self.__red) + "\n" +
            "Green: " + str(self.__green) + "\n" +
            "Blue: " + str(self.__blue) + "\n" +
            "Distancia: " + str(self.__distancia) + "\n"
        )

p01 = Particula(id="16", origen_x="0", origen_y="2", destino_x="7", destino_y="14", velocidad="180", red="18", green="21", blue="14", distancia="")
print(p01)
p02 = Particula("17", "1", "3", "18", "54", "210", "2", "4", "6", "")
print(p02)