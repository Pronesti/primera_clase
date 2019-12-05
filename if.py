#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:31:06 2019

@author: diego
"""
#1
def decir_si_es_mas_grande_que_5() :
    numero = 10
    return numero > 5
#2
def decir_si_la_longitud_es_mayor_a_5():
    unNombre = " Camel Black "
    return len(unNombre) > 5
#3
def debe_decir_si_es_mas_grande_que( unNumero ):
    if unNumero > 10:
        return true
    else:
        return false
#4
def decir_si_es_igual_a( unNumero ):
    numero = 10
    return unNumero == numero
#5
def decir_si_la_longitud_es_igual_a( unNombre , unNumero ) :
    return len(unNombre) == unNumero

#COMBINADAS
def es_par( unNumero ):
    resto = unNumero % 2
    return resto == 0

#1
def devolver_el_valor_mas_grande( valor1 , valor2 ):
    if valor1 > valor2 :
        resultado = valor1
    else :
        resultado = valor2
    return resultado
#2
def devolver_el_doble_si_es_par( unNumero ):
    if es_par( unNumero ):
        resultado = unNumero * 2
    else :
        resultado = unNumero
    return resultado
#3
def devolver_segun_condiciones_locas( unNumero ):
    if ( unNumero == 2) :
        resultado = unNumero + 1
    elif ( unNumero <= 10) :
        resultado = unNumero * 2
    elif unNumero > 20 and unNumero < 34
        resultado = unNumero + 5
    else :
        resultado = 0
    return resultado

## mas ejercicios para practicar

#1
def doble_si_menor_20_mayor_10(unNumero):
    if unNumero > 10 and unNumero < 20:
        resultado = unNumero * 2
    else:
        resultado = unNumero
    return resultado

#2
def rayos_si_menor_5_mayor_20(unNumero):
    if unNumero > 20 or unNumero < 5:
        resultado = "Rayos y Centellas"
    else:
        resultado = ""
    return resultado
#3
def rango_deseado(unNumero):
    if unNumero > 5 or unNumero < 10:
        resultado = "Rango deseado"
    else:
        resultado = "Fuera de rango"
    return resultado
#4
def numero_muy_grande(unNumero):
    if unNumero < 5:
        resultado = "Menor a 5"
    elif unNumero > 10 and unNumero < 20:
        resultado = "Entre 10 y 20"
    else:
        resultado = "Numero muy grande"
    return resultado
