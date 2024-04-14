from textwrap import indent
import pandas as pd 

data_ejemplo = {
    "Nombre": ["Carlos", "María", "Javier", "Lucía", "Sara", "Daniel"],
    "Ciudad": ["Madrid", "Barcelona", "Sevilla", "Valencia", "Barcelona", "Madrid"],
    "Edad": [28, 35, 40, 22, 31, 37],
    "Puntuacion": [85, 92, 78, 85, 88, 90]
}

df_data = pd.DataFrame(data_ejemplo)


"""
Agregar múltiples filas al DataFrame: Modifica el código para agregar múltiples filas al DataFrame df_data. Puedes crear una lista de diccionarios donde cada diccionario represente una fila y luego utilizar un bucle para agregar estas filas al DataFrame.
"""
lista_diccionarios = [
    {"Nombre": "Ana", "Ciudad": "Madrid", "Edad": 25, "Puntuacion": 80},
    {"Nombre": "Juan", "Ciudad": "Barcelona", "Edad": 33, "Puntuacion": 90},
    {"Nombre": "Luis", "Ciudad": "Madrid", "Edad": 30, "Puntuacion": 85},
    {"Nombre": "Laura", "Ciudad": "Valencia", "Edad": 28, "Puntuacion": 88},
    {"Nombre": "Pedro", "Ciudad": "Barcelona", "Edad": 45, "Puntuacion": 75},
    {"Nombre": "Carla", "Ciudad": "Madrid", "Edad": 39, "Puntuacion": 91}
]

def agregacion_filas(fila_dicts, df_data):
    for item in fila_dicts:
        new_row = pd.Series(item)
        df_data = pd.concat([df_data, new_row.to_frame().T], ignore_index=True)
    return df_data

df_filas = agregacion_filas(lista_diccionarios, df_data).copy()
print("*"*40)
print(df_filas)

"""
Eliminar filas del DataFrame: Crea una función que elimine una fila específica del DataFrame df_data basándote en algún criterio, como el nombre o la edad de una persona.
"""
def eliminacion_fila(df, columna, item):
    df= df.drop(df[df[columna] == item].index)
    return df

df_eliminacion = eliminacion_fila(df_filas, "Nombre", "Carla")
print("*"*40)
print(df_eliminacion)

"""
Modificar valores en el DataFrame: Escribe un código para modificar el valor de una celda específica en el DataFrame df_data. Por ejemplo, puedes cambiar la ciudad de una persona de "Madrid" a "Barcelona".
"""
def edicion_df_nombre (df, columna, item_referencia, nuevo_item):
    df.loc[df["Nombre"] == item_referencia, columna] = nuevo_item
    return df

def edicion_de_ciudad (df, columna, item_referencia, nuevo_item):
    df.loc[df["Ciudad"] == item_referencia, columna] = nuevo_item
    return df

df_editado = edicion_df_nombre(df_filas, "Ciudad", "Pedro", "hola")
print("*"*40)
print(df_editado)

"""
Ordenar el DataFrame por una columna: Ordena el DataFrame df_data por la columna "Edad" en orden ascendente. Luego, imprime el DataFrame ordenado.
"""

df_edad_ordenada = df_filas.sort_values(by=["Edad"],ignore_index=True, ascending=[True])
print("*"*40)
print(df_edad_ordenada)

"""
Agrupación y Agregación:
Agrupa el DataFrame por ciudad y calcula el promedio de edad y puntuación para cada ciudad.
"""
df_agrupacion = df_filas.groupby("Ciudad").agg({"Edad":"mean", "Puntuacion": "mean"})
print("*"*40)
print(df_agrupacion)

"""
Operaciones de Filtrado y Modificación:
Reemplaza todos los valores de "Madrid" en la columna "Ciudad" con "MAD".
Elimina todas las filas donde la edad sea menor que 25.
Crea una nueva columna llamada "Calificación" que sea el doble de la columna "Puntuacion".
"""
df_ciudad_editada = edicion_de_ciudad(df_filas, "Ciudad", "Madrid", "MAD")
print(df_ciudad_editada)

df_eliminacion_edad = df_ciudad_editada[df_ciudad_editada["Edad"] > 30]
print(df_eliminacion_edad)

df_eliminacion_edad["CalificaciónD"] = df_eliminacion_edad["Puntuacion"] * 2
print(df_eliminacion_edad)

