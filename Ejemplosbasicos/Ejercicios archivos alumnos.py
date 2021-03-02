# with open("Contenido\Ejemplos básicos\quijote.txt", encoding="utf8") as archi: # archi es una referencia a un objeto de la clase File      
#    ant = 0 #verificador
#    for linea in archi:
#        cuantas = len(linea)       
#        if cuantas > 1 :                
#            ant = 0
#            linea=linea.rstrip()
#            print(linea)
#        elif cuantas <= 1 and ant == 0: #el verificador me permite imprimir un linea en blanco y sacar las repetidas
#            print(linea)
#            ant = 1

# with open("Contenido\Ejemplos básicos\quijote.txt", encoding="utf8") as archi:
#     for linea in archi:
#         print(linea.rstrip()[::-1])

def buscapal(arch, pal):
    with open(arch, encoding="utf8") as archi:
        cont = 0
        for linea in archi:
            cuantos = linea.count(pal)
            if cuantos > 0:
                cont += 1
        return cont

def file3(archi, pal):
    with open(archi, mode="tr", encoding="utf8") as entrada:
        texto=entrada.read()
    
    palabras=texto.split()
    return palabras.count(pal)

print("la palabra se repite :",buscapal("Contenido\Ejemplos básicos\quijote.txt", "en"), "veces")