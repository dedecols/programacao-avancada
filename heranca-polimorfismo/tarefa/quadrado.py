from retangulo import Retangulo

class Quadrado(Retangulo):
    def __init__(self, x1, y1, lado):
        # O construtor de Quadrado informa o valor de x2 e y2 a partir do valor de lado
        x2 = x1 + lado
        y2 = y1 + lado
        # Envia os valores para o construtor da classe pai, Retangulo
        super().__init__(x1, y1, x2, y2)

    # Atributo lado
    @property
    def lado(self):
        return self.x2 - self.x1
    
    @lado.setter
    def lado(self, lado):
        if lado>0:
            self._x2 = self._x1 + lado
            self._y2 = self._y1 + lado
        else:
            print("O lado precisa ser positivo!")


quadrado1 = Quadrado(x1=0.0, y1=0.0, lado=1.0)
quadrado1.x1
quadrado1.y1
quadrado1.x2
quadrado1.y2
quadrado1.__str__()
quadrado1.area()
quadrado1.perimetro()

quadrado2 = Quadrado(x1=1, y1=1, lado=7)
quadrado2.__str__()
quadrado2.area()
quadrado2.perimetro()
