import math as m
from newton_rhapson import method_newton_raphson
from bisection import bissect
from false_position import method_falseposition

def f(x):
  return x**3 + 3*x

def d(x):
  return 3 *  x ** 2 + 3

def main():
  escolha1 = int(input("Digite 1 para escoher o Método de Newton-Rhapson \n Digite 2 para escoher o Método da Bisseção \n Digite 3 para escolher o Método da Falsa Posição: "))
  if escolha1 < 1 or escolha1 > 3:
    print("Digite um número válido!!!!!")
    return main()
  
  elif escolha1 == 1:
    x0 = float(input("Digite o ponto inicial em que o método comecará: "))
    maxiter = int(input("Digite o número máximo de iterações que o método realizará: "))
    eps = float(input("Digite o erro epsilon para o intervalo entre as iterações: "))
    x,k = method_newton_raphson(f,d,x0,maxiter,eps)
    print(f"A raíz da função é x = {x}, o número de iterações que o método levou é {k}")
  
  elif escolha1 == 2:
    x0 = float(input("Digite o primeiro ponto do intervalo: "))
    x1 = float(input("Digite o segundo ponto do intervalo: "))
    eps = float(input("Digite o erro epsilon para o intervalo entre as iterações: "))
    x,k = bissect(f,x0,x1,eps)
    print(f"A raíz da função é x = {x}, o número de iterações que o método levou é {k}")

  else:
    x0 = float(input("Digite o primeiro ponto do intervalo: "))
    x1 = float(input("Digite o segundo ponto do intervalo: "))
    eps = float(input("Digite o erro epsilon para o intervalo entre as iterações: "))
    maxiter = int(input("Digite o número máximo de iterações que o método realizará: "))
    x,k = method_falseposition(f,x0,x1,eps,maxiter)
    print(f"A raíz da função é x = {x}, o número de iterações que o método levou é {k}")

main()
  