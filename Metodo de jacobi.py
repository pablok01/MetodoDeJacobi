import numpy as np
#Definimos la matriz T
T=np.array([[0,1/10,-1/5,0],[1/11,0,1/11,-3/11],[-1/5,1/10,0,1/10],[0,-3/8,1/8,0]])
c=np.array([3/5,25/11,-11/10,15/8])
x=np.array([0,0,0,0]) #Vector de valores iniciales
erroraceptado=0.0005
error=1
print('Iteraciones')
print("      x1           x2          x3          x4")
while error>erroraceptado:
    resultado=np.dot(T,x)+c
    print(resultado)
    numerador=np.amax(abs((resultado-x)))
    denominador=np.amax(abs(resultado))
    error=numerador/denominador
    x=resultado
print()
print()
print('los valores buscados que dan solucion son:')
print("      x1           x2          x3          x4")
print(resultado)