class Retangulo:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    # Atributo 1: x1
    @property
    def x1(self):
        return self._x1

    @x1.setter
    def x1(self, x1):
        # if type(x1) == float and x1>=0: self._x1 = x1
        if isinstance(x1, (int, float)) and x1>=0: self._x1 = x1
        else: print("A entrada para x1 está incorreta!")

    # Atributo 2: y1
    @property
    def y1(self):
        return self._y1

    @y1.setter
    def y1(self, y1):
        # if type(y1) == float and y1>=0: self._y1 = y1
        if isinstance(y1, (int, float)) and y1>=0: self._y1 = y1
        else: print("A entrada para y1 está incorreta!")

    # Atributo 3: x2
    @property
    def x2(self):
        return self._x2
    
    @x2.setter
    def x2(self, x2):
        # if type(x2) == float and x2>=0 and x2>self.x1: self._x2 = x2
        if isinstance(x2, (int, float)) and x2>=0 and x2>self.x1: self._x2 = x2
        else: print("A entrada para x2 está incorreta! Precisa ser maior ou igual a zero e x2 precisa ser maior que x1.")

    # Atributo 4: y2
    @property
    def y2(self):
        return self._y2

    @y2.setter
    def y2(self, y2):
        # if type(y2) == float and y2>=0 and y2>self.y1: self._y2 = y2
        if isinstance(y2, (int, float)) and y2>=0 and y2>self.y1: self._y2 = y2
        else: print("A entrada para y2 está incorreta! Precisa ser maior ou igual a zero e y2 tem que ser maior que y1.")

    def largura(self):
        largura_medida = round(self.x2 - self.x1, ndigits=2)
        return largura_medida

    def altura(self):
        altura_medida = round(self.y2 - self.y1, ndigits=2)
        return altura_medida

    def area(self):
        area_medida = round(self.largura() * self.altura(), ndigits=2)
        return area_medida

    def perimetro(self):
        perimetro_medida = round(2*(self.largura()+self.altura()), ndigits=2)
        return perimetro_medida

    # Método descrito como "human-readable string representation of an object"
    # Usa f-strings (formatted string literals), que facilita o uso de strings e variáveis juntas
    # o f sinaliza que o python deve procurar expressões dentro das chaves e processá-las
    # as aspas delimitam o início e fim do texto
    # as chaves são espaços reservados (placeholders), o que está dentro é código python
    def __str__(self):
        return f"({self.x1},{self.y1}) e ({self.x2},{self.y2})"

retangulo = Retangulo(x1=1.1, y1=2.2, x2=3.3, y2=4.4)
# retangulo.x1
# retangulo.y1
# retangulo.x2
# retangulo.y2

retangulo.__str__()
retangulo.largura()
retangulo.altura()
retangulo.area()
retangulo.perimetro()



retangulo2 = Retangulo(x1=1,y1=3,x2=2,y2=7)
retangulo2.__str__()
retangulo2.largura()
retangulo2.altura()
retangulo2.area()
retangulo2.perimetro()

