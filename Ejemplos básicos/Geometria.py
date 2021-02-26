import math
class Figura():
    def __init__(self, nombre):
        self.__nombre=nombre
        self.__x=0
        self.__y=0

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre=valor
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, valor):
        self.__x=valor

    def superficie(self):
        pass

    def perimetro(self):
        pass

    def __str__(self): #Me permite definir una conversión a string del objeto
        return "Figura: {​​​​​}​​​​​ - Superficie: {​​​​​}​​​​​ - Perimetro: {​​​​​}​​​​​".format(self.nombre, self.superficie(), self.perimetro())

class Circulo(Figura):
    def __init__(self, radio): #Sobreescribo un método de mi clase padre
        super().__init__("Circulo")
        self.__radio=radio
        
    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, valor):
        self.__radio=valor
    
    def superficie(self):
        return math.pi*self.radio**2

    def perimetro(self):
        return math.pi*2*self.radio
        
    def __str__(self): #Sobreescribo la clase de mi padre
        return super().__str__()+" - Diámetro: {​​​​​}​​​​​".format(self.radio)