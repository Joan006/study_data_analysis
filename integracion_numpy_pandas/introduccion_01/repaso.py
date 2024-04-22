import pandas as pd 
import numpy as np 


pd.set_option('display.max_rows', None)  # Muestra todas las filas
pd.set_option('display.max_columns', None)  # Muestra todas las columnas

"""
Crear un DataFrame de Pandas desde un diccionario:
Crea un diccionario con datos adicionales y úsalo para crear un nuevo DataFrame de Pandas.
Imprime el DataFrame para verificar los datos.
"""

data = {
    "Nombre": ["Juan", "Ana", "Luis", "Laura"],
    "Edad": [25, 33, 30, 28],
    "Ciudad": ["Madrid", "Barcelona", "Madrid", "Barcelona"],
    "Puntuacion": [80, 90, 85, 88]
}

df = pd.DataFrame(data)

"""
Operaciones de Estadísticas Descriptivas:
Calcula la suma de cada columna en el DataFrame utilizando tanto NumPy como Pandas.
Calcula la mediana de cada columna en el DataFrame utilizando tanto NumPy como Pandas.
"""

suma_pd = df[["Edad", "Puntuacion"]].sum()
print(suma_pd)
print("*"*50)

suma_np_1 = np.sum(df["Edad"].values)
suma_np_2 = np.sum(df[["Puntuacion"]].values)
print(suma_np_1, suma_np_2)
print("*"*50)
"""
Manipulación de Datos:
Agrega una nueva columna al DataFrame existente, por ejemplo, una columna "D" con valores arbitrarios.
Elimina una columna del DataFrame.
Cambia el nombre de una columna en el DataFrame.
"""
# agregamos una columna 
df["Sexo"] = ["M", "F", "M", "F"]
print(df)
print("*"*50)
# eliminacion de columna Puntuacion
df = df.drop("Puntuacion", axis=1)
print(df)
print("*"*50)

# cambio de nombre
df = df.rename(columns={"Edad": "edad"})
print(df)
print("*"*50)
"""
Indexación y Selección:
Selecciona solo las filas donde el valor de la columna "A" es mayor que 1.
Selecciona solo las filas donde el valor de la columna "B" es par.
Selecciona la fila con el índice 1 y todas las columnas.
"""

df_edad = df[df["edad"] > 25]
print(df_edad)
print("*"*50)

"""
Operaciones con NumPy:
Crea un array de NumPy aleatorio de tamaño 3x3.
Multiplica cada elemento del DataFrame por el correspondiente elemento del array de NumPy.
Suma el array de NumPy a cada fila del DataFrame.
"""
# Crea un DataFrame de pandas de ejemplo de tamaño 3x3
df_2 = pd.DataFrame({
   'A': [1, 2, 3],
   'B': [4, 5, 6],
   'C': [7, 8, 9]
})
array_random = np.random.rand(3,3)
print(array_random)

df_2 = df_2 * array_random
print(df_2)

df_2 = df_2 + array_random
print(df_2)

"""
Agregación y Agrupación:
Agrupa el DataFrame por la columna "A" y calcula la media de cada grupo.
Agrupa el DataFrame por la columna "B" y calcula la suma de cada grupo.
Agrupa el DataFrame por la columna "C" y calcula la mediana de cada grupo.
"""
df["numeros"] = [20, 34, 34, 43]
print(df)

categoria_ciudad= df.groupby(["Sexo", "Ciudad"])
print(categoria_ciudad.groups)

operacion_agrupada = categoria_ciudad.agg(
    {
        "edad": "mean",
        "numeros": "sum"
    }
)
print(operacion_agrupada)


"""
Modifica el código para calcular la media de la columna "edad" en lugar de la suma.
Agrega una nueva columna al DataFrame que represente la suma de la columna "edad" y la columna "numeros" para cada fila.


"""

df["sumas"] = df[["edad", "numeros"]].sum(axis=1)
print(df)

"""
Realiza una operaci√≥n de agregaci√≥n para calcular tanto la suma como el promedio de la columna "numeros" agrupado por "Sexo" y "Ciudad".
"""
agrupacion_2 = df.groupby(["Sexo", "Ciudad"]).agg(
    {
        "numeros": ["sum", "mean"]
    }
)

print(agrupacion_2)

"""
Filtra el DataFrame para mostrar solo las filas donde el valor de la columna "numeros" sea mayor que 30.
"""

df_filtro_nums = df[df["numeros"] > 30]
print(df_filtro_nums)

"""
Crea una nueva columna que indique si el valor de la columna "edad" es mayor que 30 o no.
"""

df["Es > 30"] = np.where(df["edad"] > 30, "si", "no")
print(df)

