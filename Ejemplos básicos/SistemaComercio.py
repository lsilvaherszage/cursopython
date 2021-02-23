import Productos as pr

lista=[]
lista.append(pr.Producto("tomate", 24.3, "almacén"))
lista.append(pr.Producto("manzana", 90, "frutas"))
lista.append(pr.Producto("pritty", 56, "bebidas"))

for pro in lista:
    print(pro)


# lista.append(pr.Bebida("teem", 33, 2))

#print(lista[3].categoria)
#print(lista[3].capacidad) #Sabe algo más, sabe hacer algo más. Bebida es un Producto pero con algunos atributos y métodos adicionales
#print(lista[2].capacidad)

#lista.append(pr.Electronico("monitor", 56000))
#print(lista[4].vf())

#print("Ahora viene la lista con productos de subclases")
#for pro in lista:
# print(pro)

