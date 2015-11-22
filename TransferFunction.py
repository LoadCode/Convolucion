#-*-coding: utf-8 -*-
#Código para el objeto función de transferencia en Python

class TransferFunction:

    num = []
    den = []
    variable = 's'
    Ts = 0

    def __init__(self, _num, _den, _Ts = 0, _variable = 's'):
        self.num = _num
        self.den = _den
        self.Ts  = _Ts
        self.variable = _variable
        

    def Visual(self):
        numer = self.Pol(self.num)
        denom = self.Pol(self.den)
        N = len(denom)+6
        print numer.center(N,' ')
        print '-'*N
        print denom.center(N,' ')

    def Pol(self,vec):
        #Esta función retorna el polinomio indicado en forma de cadena para su representación

        N = len(vec)
        n = N-1  #Orden del polinomio
        pol = ''

        if self.variable == 's':
            var = 'S'
        elif self.variable == 'z':
            var = 'z'
        
        for k in range(0,N):
            if n > 0:
                if vec[k] == 1:
                    if n != 1:
                        pol += var+'^'+str(n)+'+'
                    else:
                        pol += var+'+'
                elif vec[k] == 0:
                    n -= 1
                    continue
                else:
                    if n != 1:
                        pol += str(vec[k])+var+'^'+str(n)+'+'
                    else:
                        pol += str(vec[k])+var+'+'
            else:
                if vec[k] != 0:
                    pol += str(vec[k])
                else:
                    n -= 1
                    pol = pol[0:len(pol)-1]
                    continue
            n -= 1
            
        return pol    
    
    

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def str2list(cad):
    strlst = cad.split(',')
    N = len(strlst)
    lista = [0 for x in range(0,N)]
    for n in range(0,N):
        lista[n] = num(strlst[n])
    return lista
        
    


#tf = TransferFunction([1,0,2,4,3],[4,3,2,1,5,4,2,3,2,4,5,3],0,'z')
#tf = TransferFunction([9],[1,1.5,9])
#tf.Visual()
