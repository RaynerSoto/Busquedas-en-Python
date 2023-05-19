#Algoritmo de búsqueda tonta
import random
import time


def busqueda_nativa(lista,objetivo):
    for x in range(len(lista)):
        if lista[x] == objetivo:
            return x
    return -1

#Algoritmo de búsqueda binaria
def busquera_binaria(lista,objetivo,limite_superior = None,limite_inferior = None):
    if limite_inferior is None:
        limite_inferior = 0
    if limite_superior is None:
        limite_superior = len(lista)-1

    if limite_inferior > limite_superior:
        return -1

    punto_medio = (limite_superior+limite_inferior)//2
    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busquera_binaria(lista,objetivo,limite_inferior,punto_medio-1)
    else:
        return busquera_binaria(lista, objetivo, limite_inferior + 1, punto_medio)


def prueba_algoritmo():
    lista = [1,2,3,4,5,66,1,2,3,4,5,6,9,11,10,12]
    print(busqueda_nativa(lista,-12))
    print(busquera_binaria(lista,66))
prueba_algoritmo()