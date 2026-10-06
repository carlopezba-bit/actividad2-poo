class Rectangulo:
    """
    Clase que define objetos de tipo Rectangulo
    con una base y una altura como atributos.
    """

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (2 * self.base) + (2 * self.altura)