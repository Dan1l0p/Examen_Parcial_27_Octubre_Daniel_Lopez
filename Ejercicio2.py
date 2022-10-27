lista = [18, 50, 210, 80, 145, 333, 70, 30]

def crear_tabla(tamanio):
    tabla = [None]* tamanio
    return tabla

def cantidad_elementos(tabla):
    return len(tabla)- tabla.count(None)

def cantidad_elementos(tabla):
    return sum(tamanio(lista) for lista in tabla if lista is not None)

def funcion_hash(dato, tamanio_tabla):
    return len(str(dato).strip()) % tamanio_tabla

def agregar(tabla, dato):
    posicion = funcion_hash(dato , len(tabla))
    if (tabla[posicion] is None):
        tabla[posicion]= dato
    else:
        print("se produjo una colision.")



