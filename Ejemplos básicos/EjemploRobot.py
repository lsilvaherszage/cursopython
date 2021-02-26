# Utilizando decoradores para getters y setters
class Robot:

    def __init__(self, x, y, rot):
        self.__x=x
        self.__y=y
        self.__rot=rot
        self.__movimientosFuturos=[]

    @property
    def movimientosFuturos(self):
        cad=" "
        return cad.join(self.__movimientosFuturos)

    @movimientosFuturos.setter
    def movimientosFuturos(self, movs):
        self.__movimientosFuturos=movs.split()
    
    def hacerMovimiento2(self):
        #Antes era un choclo...
        print("casa")
        # if len(self.__movimientosFuturos)==0:
        #     return "No hay movimientos"
        # else:
        #     return self.__movimientosFuturos.pop()

# Usando getters y setter parece que estoy accediendo directamente al atributo, pero en realidad lo tengo desacoplado por métodos.

r.movimientosFuturos="Derecha Arriba Derecha"
# print(r.movimientosFuturos)
print(r.hacerMovimiento2())
# print(r.hacerMovimiento())
# print(r.hacerMovimiento())
# print(r.hacerMovimiento())