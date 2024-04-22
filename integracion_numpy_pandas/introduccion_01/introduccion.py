import pandas as pd 
import numpy as np 

# Crearemos un DATAFRAME apartir de un array de numpy

# creamos array np
data = np.array([[1,2,3], [4,5,6], [7,8,9]])

# creamos df pd 
df = pd.DataFrame(data, columns=["A", "B", "C"])
print(df)

# Convertir un df a un array de numpy
data_2 = {
    "A":[1,2,3],
    "B":[2,34,5],
    "C":[3,6,7]
}
df_2 = pd.DataFrame(data_2)
arr = df_2.to_numpy()

# algunas funciones las comparten ambas librerias 
mean_filas_np = np.mean(df_2, axis=0)   # axis = 0 (filas), axis=1(columns)
print(mean_filas_np)

# hace la misma operacion con pd
mean_filas_pd = df_2.mean()
print("*"*40)
print(mean_filas_pd)

