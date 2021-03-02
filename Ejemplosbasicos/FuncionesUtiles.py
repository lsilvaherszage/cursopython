from math import sqrt
def cuadradoPerfecto(valor):
    return int(sqrt(valor))==sqrt(valor)

def enElMismoOrden(texto, listaPalabras):
    lista=texto.split()
    try:
        resu=[lista.index(pal) for pal in listaPalabras]
        if sorted(resu)==resu:
            resuFinal=True
        else:
            resuFinal=False
    except:
        resuFinal=False
    return resuFinal