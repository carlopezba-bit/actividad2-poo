import math


class TrianguloRectangulo:
    """
    Clase que define objetos de tipo TrianguloRectangulo
    con una base y una altura como atributos.
    """

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self):
        return math.pow(
            self.base * self.base + self.altura * self.altura,
            0.5
        )

    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()

        if (
            self.base == self.altura
            and self.base == hipotenusa
            and self.altura == hipotenusa
        ):
            print("Es un triángulo equilátero")

        elif (
            self.base != self.altura
            and self.base != hipotenusa
            and self.altura != hipotenusa
        ):
            print("Es un triángulo escaleno")

        else:
            print("Es un triángulo isósceles")