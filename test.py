import convolucion as conv

a = [1,0.5,3]
b = [1,0.5,-3]

y = conv.convolucion(b,a)
#print y



def poly(polo_1, polo_2):
    poli = conv.convolucion([1, polo_1[0], polo_1[1]], [1, polo_2[0], polo_2[1]])
    poli[2] = poli[2]-poli[4]
    poli = poli[0:3]
    poli[1] *= -1
    return poli


#Obtener los coeficientes de un polinomio a partir de sus raices

# s^2+s+9.25    polos = -0.5+-J3
# s^2+3s-1      polos = 0.302775638   -3.302775638
# s^2-2s+1      polos = 1
# s^2-9s+0.5    polos = -0.5+-J3
sig = -0.5;            w = 3;
Polo_1 = [0.302775638, 0]
Polo_2 = [-3.302775638, 0]

Polinom = poly(Polo_1, Polo_2)

print Polinom
