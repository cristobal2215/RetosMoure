class calculadora:
    def __init__(self, base, altura):
        self.base = 5
        self.altura = 5

    def Triangulo(self):
        area = self.base * self.altura /2
        print('area del triangulo ', area)

    def Cuadrado(self):
        area = self.base**2
        print('area del cuadrado ', area)

    def Rectangulo(self):
        area = self.base * self.altura
        print('area del rectangulo', area)

calculadora = calculadora(5, 5)
calculadora.Triangulo()
calculadora.Cuadrado()
calculadora.Rectangulo()