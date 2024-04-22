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

# crear una matriz de identidad 
arr_identidad = np.eye(6)

# Creacion de matriz (2,3,4)
arr_3d = np.zeros((2,3,4))
print("*"*40)
print(arr_3d)

# Tansponer una matriz 

arr_t = np.random.rand(2,5)
print(arr_t.T)

# concatenar matrizes horizontalmente
arr_1 = np.array([[1,2], [3,4]])
arr_2 = np.array([[6,7],[8,9]])

arr_h = np.hstack((arr_1, arr_2))
print(arr_h)
