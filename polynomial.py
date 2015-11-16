# -*-coding: utf-8 -*-

# FUNCIÓN POLY() EN PYTHON PARA HALLAR LOS COEFICIENTES DEL POLINOMIO DADAS SUS RAICES

# @Author: Julio César Echeverri Marulanda
# @E-mail: julio.em7@gmail.com

from convolucion import *

def poly(roots):
    #Esta función retorna un vector con los coeficientes de un polinomio que corresponde
    #a la lista de polos o raices dadas en 'Polos'
    orden = len(roots)
    poli = [0 for x in range(0,orden)]
    poliaux = -roots[0]
    for k in range(0,orden-1):
        if k == 0:
            poli[k+1] = convolucion([1,poliaux],[1,-roots[k+1]])
        else:
            poli[k+1] = convolucion(poliaux,[1,-roots[k+1]])
        poliaux = poli[k+1]

    for k in range(0,len(poliaux)):
        if poliaux[k].imag == 0:
            poliaux[k] = poliaux[k].real
    
    return poliaux



#Ejemplo de uso de la función poly en Python
print poly([-0.5+3*1j, -0.5-3*1j, 4])

