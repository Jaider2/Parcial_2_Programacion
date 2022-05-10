import numpy as np
import sys
from numpy.polynomial.polynomial import Polynomial
import random as rm

mensaje_1="Ingrese el grado que tendra el polinomio: "
mensaje_2="El número no es natural, por favor ingrese un número correcto: "
mensaje_3="Ingrese los valores de los coeficientes en orden ascendente incluyendo ceros: "
mensaje_7="Ingrese un valor aproximado de la raíz: "
mensaje_4="\nEstas son las raices del polinomio:"
mensaje_5="\nEstas son las aproximaciones de una de las raices del polinomio: "
mensaje_6="\nEstas es la raíz del polinomio: "
mensaje_8="\nEste es el polinomio ingresado: "

n=eval(input(mensaje_1))
N=n+1
#Condicional para tipo de número N ingresado
if N!=int(N):
    print(mensaje_2)
    sys.exit()
if N<0:
    print(mensaje_2)
    sys.exit()

#Definimos una lista vacia
A=[]

#Disponemos un ciclo de N vueltas
for y in range(N):
    valor=int(input(mensaje_3))
    A.append(valor)

#Creamos la lista B
B_1 = list(range(0,N))
B_2 = np.multiply(A,B_1)
B = B_2[1:]
B_in = B[::-1]

#Definimos la funcion y su derivada
funcion_1 = Polynomial(A)
funcion_derivada = Polynomial(B)

#Definimos un x_n conveniente
New = A[::-1]
Raices = np.roots(New)
Valor_pre = rm.choice(Raices)
def x_n(Valor_pre):
    return Valor_pre + 1
#x_n=eval(input(mensaje_7))

#Procedimiento
tabla = []
xi = x_n(Valor_pre)
#xi = x_n
for n in range (4):
    f_1 = np.polyval(New,xi)
    f_2 = np.polyval(B_in,xi)
    xnuevo = xi - f_1/f_2
    tabla.append([xnuevo])
    xi = xnuevo
    if xnuevo in Raices:
        break
tabla = np.array(tabla)

#Salidas
#print(mensaje_4)
#print(Raices)
print(mensaje_8)
print(funcion_1)
if len(tabla)==1:
    print(mensaje_6)
else:
    print(mensaje_5)
print(tabla)




