import struct
import os
import sys


def fun1(cade):
    lista=[]
    aux=""
    for car in cade:
        aux+=car
        if len(aux)==2:
            lista.append(aux)
            aux=""
    if len(aux)==1: lista.append(aux+"_")
    return lista

def fun1Recursivo(param):
    if len(param)<=2:
        return [(param+"_")[:2]]
    else:
        return [param[:2]]+fun1Recursivo(param[2:])

def fun2(cadena):
    cont=0
    for car in cadena:
        if car==".":
            cont+=1
        else:
            break
    return cont

def fun3(nume, valor):
    lista=list(nume)
    aux=[abs(ele-valor) for ele in lista]
    return(lista[aux.index(min(aux))])

def fun4(cadena):
    if cadena[-1]!=".":
        cadena=cadena+"."
    if not cadena[0].isupper():
        cadena=cadena[0].upper()+cadena[1:]
    return cadena

def fun5(cadena):
    lista=cadena.split()
    nueva=[pala[::-1] for pala in lista]
    return " ".join(nueva)

def fun6(cadena):
    cont=0
    for car in cadena:
        if car.isdigit(): cont +=1 
    return cont

def fun7(top, *tupla):
    
    def clave(ele):
        return ele["pre"]
    
    lista=list(tupla)
    lista.sort(key = clave, reverse=True)
    return lista[:top]

def fun7bis(listaDict, numero):
    newlist = sorted(listaDict, key=lambda k: k['pre']) 
    return (newlist[-numero:])

def fun8(c1, c2):
    pos=c1.find(c2)
    if pos!=-1:
        caux=c1[pos+len(c2):]
        pos2=caux.find(c2)
    
    if pos==-1 or pos2==-1:
        return None
    else:
        return pos2+pos+2

C1 = "Esto es una estatua estable"
C2 = "st"
def busca(esto, enesto):
    no = enesto.rfind(esto)
    return no

# print(busca(C2, C1))

#print(fun1("cas"))
#print(fun1Recursivo("este es un ejemplar"))
#print(fun2("casa"))
#print(fun3({5,11,77,22},9)).
#print(fun4("casa..."))
#print(fun5("Este es un ejemplo interesante"))
#print(fun6("Esto tiene 2 digitos dentro de 20 caracteres"))
#print(fun7(2, {"prod":"pan", "pre": 100}, {"prod":"arroz", "pre": 50}, {"prod":"leche", "pre": 90}, {"prod":"carne", "pre": 300}, {"prod":"pasta", "pre": 350}))
#print(fun8("Esto es un ejemplo estándar", "st"))

print(os.path.dirname(sys.executable))