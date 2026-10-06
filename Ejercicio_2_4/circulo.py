import math


class Circulo:
    """
    Clase que define objetos de tipo Circulo
    con su radio como atributo.
    """

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio