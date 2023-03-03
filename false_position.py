"""
Método da falsa posição que recebe uma função, um intervalo,
um erro epsilon, um número máximo de iterações e retorna uma raíz real
e o número de iterações que o método levou
"""

def method_falseposition(f ,x0 , x1,eps,maxit):
    k = 1    
    x0 = x0
    x1 = x1
    xtol = ftol = eps  
    if(f(x0)*f(x1)>0):  return ("O intervalo especificado não possui uma raíz", 0)
    if (abs(x0-x1)<eps):  return("Raíz já encontrada", 0)

    while (True):
            
        x = ( ((x0*f(x1)) - (x1*f(x0)) )/(f(x1) - f(x0))  )
        intervalx = abs(x1-x0)
        if ( f(x0) * f(x) > 0 ): x0 = x
        else                  : x1 = x

        if ( k == maxit ):    break
        if ( abs(x1-x0)  < xtol ): break
        if ( abs(f(x)) < ftol ): break
        k+=1
    return (x,k)
