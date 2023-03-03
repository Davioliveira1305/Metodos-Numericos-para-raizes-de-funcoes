"""""
Método de Newton-Rhapson que recebe uma função, 
sua derivada, número máximo de iterações, um erro epsilon, um ponto inicial,
e retorna uma raíz real e o número de iterações que o método levou
""" 
def method_newton_raphson(f,d,x0,maxiter,e):
  k = 1
  while(True):
    x = round(x0 - (f(x0)/d(x0)),6)
    print(f"===========Iteração{k}===========")
    print(f"x0={x0}, x={x} ")
    if(abs(f(x))<e):
      break
    print(f"|f(x)|={abs(f(x))}")
    if(abs(x-x0)<e):
      break
    print(f"|x-x0|={abs(x-x0)} \n")
    x0 = x
    k = k+1
    if (k==maxiter):
      break

  return (x,k)