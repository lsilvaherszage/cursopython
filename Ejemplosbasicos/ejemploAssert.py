import random

def foo():
    return random.randint(-1,1)


valor=foo()
assert valor>=0, "Foo retornĂ³ un valor negativo: {}".format(valor)
print ("El valor retornado por foo es: {}".format(valor))