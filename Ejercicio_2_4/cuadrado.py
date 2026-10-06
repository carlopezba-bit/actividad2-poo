class Cuadrado:
    """
    Clase que define objetos de tipo Cuadrado
    con un lado como atributo.
    """

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado