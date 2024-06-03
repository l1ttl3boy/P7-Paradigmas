import math

class Punto3D:
    def __init__(self, x=4, y=10, z=2):
        self.__x = x
        self.__y = y
        self.__z = z

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_z(self):
        return self.__z

    def set_z(self, z):
        self.__z = z

    def distancia(self, otro_punto):
        dx = self.__x - otro_punto.get_x()
        dy = self.__y - otro_punto.get_y()
        dz = self.__z - otro_punto.get_z()
        distancia = math.sqrt(dx**2 + dy**2 + dz**2)
        return distancia

# Crear los 10 objetos de tipo Punto3D
puntos = [Punto3D() for _ in range(10)]

# Calcular las distancias entre todos los puntos
distancias = []
for i in range(len(puntos)):
    for j in range(i+1, len(puntos)):
        distancia = puntos[i].distancia(puntos[j])
        distancias.append(distancia)

# Determinar la menor distancia
minima_distancia = min(distancias)

print("La menor distancia entre los puntos es:", minima_distancia)
