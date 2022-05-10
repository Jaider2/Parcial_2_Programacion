# Parcial_2_Programacion
Repositorio con documentos del 2 parcial de programación

Para la creacion del programa fue necesario importar numpy, sys, polynomial y random.
El proceso de creacion del codigo fue separado por comentarios en el documento Parcial_2.py
el primer paso fue crear una variable n la cual seria el grado del polinomio el cual se le
solicitara al usuario, a este valor n le sumaremos 1 para facilidad a lo largo del codigo,
de modo que termia¿namos con la variable N=n+1.

EL siguiente paso fue a partir de condicionales restingir la entrada n solo a números
naturales, posteriormente se creo una lista vacia A y un ciclo con N vueltas donde cada
entrada seria uno de los valores de los coeficientes del polinomio, estos valores se
agregaron a la lista A, luego se creo la lista B que contiene los coeficientes de la
derivada del polinomio, tanto a la lista A como a la lista B se les crearon 2 copias
siendo las listas New y B_in respectivamente, estas se encuentran con el orden 
de los coeficientes invertidos.

Se definieron dos funciones con las listas A y B para simular las funciones del polinomio
y su respectiva derivada. se creo un x_n conveniente para el ejercicio, para esto se
encontraron las raices del polinomio con el comando numpy.roots, se seleciona una de estas
raices de manera aleatoria con el comando random.choice y a este valor le sumamos 1
para crear un valor diferente de las raices.

Este valor x_n tambien se le dio la posibilidad de ser dado por el usuario, para esto es
necesario retirar el numeral de las lineas 49 y 54, y borrar o comentar las lineas
47, 48 y 53. Con esto el vaor x_n se le preguntara al usuario. 

Para el procedimiento de las iteraciones se uso el metodo de Newton-Rhapson donde se
creo un ciclo de 4 vueltas donde se evaluava la funcion y su derivada en un valor xi=x_n
posteriormente al arrojar el resultado de la formula se le da el nombre de xnuevo, el cual
sera el nuevo valor de xi para la siguiente vuelta, los datos del xnuevo se recogeran
en una tabla vacia previamente creada, se agrega un condicional donde se busca si alguno
de los xnuevo aparece en la tabla de las raices del polinomio, en caso de no aparecer se
continuara con la siguiente vuelta, en caso de aparecer se cerrara el ciclo y solo guardara
los datos recogidos hasta este punto.

Finalmente se imprime el polinomio dado junto con las iteraciones de una de sus raices.
