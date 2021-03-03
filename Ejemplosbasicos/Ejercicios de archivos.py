# Ejercicios de archivos
"""
1. Desarrollar un programa que saque las líneas en blanco repetidas del archivo quijote.txt.
2. Desarrollar un programa que escriba cada línea de quijote.txt invertida.
3. Dado el nombre de un archivo y una palabra, devolver cuántas veces 
aparece la palabra en el archivo (como palabra, no como cadena)
"""

def file1():
    with open("Contenido\Ejemplos básicos\quijote.txt", mode="tr", encoding="utf8") as entrada:
        with open("Contenido\Ejemplos básicos\quijoteLimpio.txt", mode="tw", encoding="utf8") as salida:
            for linea in entrada:
                if linea!="\n":
                    salida.write(linea)

def file2():
    with open("Contenido\Ejemplos básicos\quijote.txt", mode="tr", encoding="utf8") as entrada:
        for linea in entrada:
            print((linea[::-1]).strip())

def file3(archi, pal):
    with open(archi, mode="tr", encoding="utf8") as entrada:
        texto=entrada.read()
    
    palabras=texto.split()
    return palabras.count(pal)

#file1()
#file2()
print(file3("Contenido\Ejemplosbasicos\quijot.txt", "en"))