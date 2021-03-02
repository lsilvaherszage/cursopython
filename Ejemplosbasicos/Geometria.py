from abc import ABC, abstractmethod
from math import pi

class Figura(ABC):
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

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, valor):
        self.__y=valor

    @abstractmethod
    def superficie(self):
        return 42

    @abstractmethod
    def perimetro(self):
        pass

    def __str__(self): #Me permite definir una conversión a string del objeto
        #QUE REPRESENTA SELF EN ESTA CLASE ABSTRACTA CUANDO LLAMO A ESTE METODO CON SUPER() DESDE UNA SUBCLASE????
        return "Figura: {} - Superficie: {} - Perímetro: {}".format(self.nombre, self.superficie(), self.perimetro())


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
        return pi*self.radio**2

    def perimetro(self):
        return pi*2*self.radio

    def __str__(self): #Sobreescribo la clase de mi padre
        return super().__str__()+" - Radio: {}".format(self.radio)
        
    
class Rectangulo(Figura):

    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.__base=base
        self.__altura=altura

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        self.__altura=valor

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, valor):
        self.__base=valor
    
    def superficie(self):
        return self.base*self.altura

    def perimetro(self):
        return self.base*2+self.altura*2

    def __str__(self): #Sobreescribo la clase de mi padre
        return super().__str__()+" - Base: {} - Altura: {}".format(self.base, self.altura)

class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)
        self.nombre="Cuadrado"
    
    def __str__(self):
        #Acá tengo la dificultad de que necesito el __str__ de Figura, y no de Rectángulo
        return super(Rectangulo, self).__str__()+" - Lado: {}".format(self.base)
    
        
