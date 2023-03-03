import math as m

#Função que calcula o número de iterações que o método da bisseção vai levar
def iteracoes(e, x, y):
    aux = e/(y-x)
    return m.ceil(-1*(m.log(aux, 2)))

"""
Método da Bisseção que recebe uma função, um intervalo, um erro epsilon
e retorna uma raíz real e o número de iterações que o método levou
"""
def bissect(f,x0,x1,eps):
    maxiter = iteracoes(eps,x0,x1)
    if(f(x0)*f(x1)>0):  return("O intervalo especificado não possui uma raíz!!!!!", 0)
    if (abs(x1-x0)<eps):  return("Raíz já encontrada!!!!!!!",0)
    k=1
    
    while(True):
        x = round((x1+x0)/2,6)
        
        if(f(x)*f(x0)<0): x1 = x
        if(f(x)*f(x1)<0): x0 = x
        
        intervaloX = abs(x1-x0)

        if intervaloX < eps: break
        if(k==maxiter):    break
        k = k+1

    return (x,k)