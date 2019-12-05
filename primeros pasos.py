#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:15:41 2019

@author: diego
"""

"""
    1)Defina una función que tome dos cadenas de caracteres como parámetro y
    devuelva la de mayor longitud. Complete el siguiente programa (la cantidad de
    guiones no indica la cantidad de caracteres a completar):
"""
def cadena_mas_larga(cadena1, cadena2):
    if len(cadena1)>len(cadena2):
        resultado = cadena1
    else:
        resultado = cadena2
    return resultado

"""
    2)Defina una función que recibe una lista y devuelve la cantidad de letras e que contiene.
"""
def cuantas_e_tiene(cadena):
    e = 0
    i= len(cadena)-1
    while i >= 0:
        if cadena[i] == "e":
            e = e + 1
        i = i - 1
    return e

"""
    3)Defina una función que tome una lista y cambie todas las vocales por -.
"""
def remover_vocales(cadena):
    i= len(cadena)-1
    while i >= 0:
        if cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u":
            cadena[i] = "-"
        i = i - 1
    return cadena
    
def desconstruir_cadena(cadena):
    i=0
    hasta=len(cadena)
    nueva_lista = []
    while i < hasta:
        nueva_lista.append(cadena[i])
        i+=1
    return nueva_lista

def unir_palabra(lista):
    i=0
    hasta=len(lista)
    palabra = ""
    while i < hasta:
        palabra = palabra + lista[i]
        i+=1
    return palabra

#res = unir_palabra(remover_vocales(desconstruir_cadena("perro")))
    
"""
    4)Defina la función mezclar que tome dos listas y devuelva una lista que sea el
    resultado de intercalas elemento a elemento. Por ejemplo: si intercalamos Pepe
    con Jose darı́a PJeopsee.
"""
def mezclar(lista_uno, lista_dos):
    long_uno = len(lista_uno)
    long_dos = len(lista_dos)
    i= 0
    if long_uno > long_dos:
        hasta = long_uno
    elif long_uno < long_dos:
        hasta = long_dos
    else:
        hasta = long_uno
    nueva_lista = [None] * hasta
    while i < hasta:
        if i < long_uno and i < long_dos:
            nueva_lista[i] = lista_uno[i] + lista_dos[i]
        elif i < long_uno:
            nueva_lista[i] = lista_uno[i]
        elif i < long_dos:
            nueva_lista[i] = lista_dos[i]
        i = i+1
    return nueva_lista
        
    