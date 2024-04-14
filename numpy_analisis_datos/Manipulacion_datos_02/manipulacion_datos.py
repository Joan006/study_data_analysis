import numpy as np 

# Crear una matriz de 2 dimensiones apartir de una lista de listas 
array_listas = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_listas)

# Crear una matriz de ceros con la dorma (3,4)
array_zeros = np.zeros((3,4))
print("*"*40)
print(array_zeros)

# modificar por indice un elemento 
array_zeros[2,2] = 10
