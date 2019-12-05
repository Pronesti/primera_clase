#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:21:50 2019
@author: diego
"""
#1
def devolver_longitud_de_un_nombre( unNombre ) :
    return len(unNombre)
#2
def devolver_el_primer_elemento_de_la_lista( unaLista):
    return unaLista[0]
#3
def devolver_segundo_elemento_del_nombre( unNombre ):
    return unNombre[1]
#4
def devolver_ultimo_elemento_del_nombre( unNombre ):
    return unNombre[len(unNombre)-1]
#5
def devolver_la_letra_en_posicion_del_nombre( unNombre, unaPosicion ):
    return unNombre[unaPosicion]
#6
def remplazar_el_ultimo_elemento_de_la_lista( unaLista, unElemento ):
    unaLista[len(unaLista)-1] = unElemento
    return unaLista
#7
def agregar_25_al_final_de_la_lista():
    _lista = ["Casa",5,"A"]
    _elemento = 25
    _lista.append(_elemento)
    return _lista
#8
def agregar_nombre_al_final_de_la_lista( unNombre ):
    _lista = ["Casa",5,"A"]
    _lista.append(unNombre)
    return _lista
#9
def primer_elemento_por_dos( unaLista ):
    unaLista[0] = unaLista[0] * 2
    return unaLista
#10
def ultimo_elemento_por_tres( unaLista ):
    unaLista[len(unaLista)-1] = unaLista[len(unaLista)-1] * 3
    return unaLista
#11
def primero_por_dos_ultimo_por_tres( unaLista ):
   return ultimo_elemento_por_tres(primer_elemento_por_dos(unaLista))
#12
def agregar_elemento_al_final_de_la_lista( unaLista, unElemento ):
    unaLista.append(unElemento)
    return unaLista