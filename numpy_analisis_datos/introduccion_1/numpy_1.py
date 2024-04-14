import numpy as np 

array1 = np.array([1,2,3,4,5,6])   # De esta manera generamos una matriz 
print(array1)
print(array1.shape)    # .shape - indica las dimensiones de la matriz


# reshape - para cambiar las dimesiones de la matriz 
arr2 = array1.reshape((2,3))
print(arr2)

# Matriz con forma de (4,4)
entre_cero_uno = np.random.rand(4,4)
print(entre_cero_uno)
