# -*- coding: cp1252 -*-

            #ALGORITMO PARA CALCULAR LA CONVOLUCI�N

#@Author: Julio C�sar Echeverri Marulanda
#@Email : julio.em7@gmail.com

#Vectores a convolucionar
a = [1,2,3]     #Vector A para la convoluci�n (puede ser >= B)
b = [3,2,4,6,1] #Vector B para la convoluci�n (puede ser >= A) 

def convolucion(a,b):
    Na = len(a)
    Nb = len(b)

    y = [0 for x in range(0,Na+Nb-1)]
    Ny = len(y)


    #Sumatoria de convoluci�n
    for n in range(0,Ny):
        k = n; f = 1;
        while k >= 0:
            if n >= Na:   #Este if es para cuando el vector que va recorriendo se sale del indice de a[k]
                k = Na-f; f += 1;
                
            y[n] += a[k]*b[n-k] #Ecuaci�n de la convoluci�n
            k -= 1
            if (n-k) >= Nb:
                break
    return y
        


