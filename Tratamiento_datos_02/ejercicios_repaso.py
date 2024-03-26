"""
Ejercicios relacionados con tratamiento de datos .1
"""

import pandas as pd
import numpy as np

"""
Tratamiento de datos faltantes:
Crea un DataFrame con datos faltantes en diferentes columnas y practica diferentes métodos para tratar esos valores faltantes, como rellenar con la media, mediana o moda, eliminar filas o columnas con valores faltantes, y reemplazar valores específicos.
"""
# Configura pandas para mostrar todas las columnas
pd.set_option("display.max_columns", None)

# Configura pandas para mostrar todas las filas
pd.set_option("display.max_rows", None)


data = {
    "ID": range(1, 21),
    "Nombre": [
        "Ana",
        "Luis",
        "Carlos",
        "María",
        "Juan",
        "Diana",
        "Jorge",
        "Elena",
        "Pedro",
        "Lucía",
        "Miguel",
        "Sofía",
        "Ricardo",
        "Carmen",
        "Fernando",
        "Laura",
        "Antonio",
        "Patricia",
        "José",
        "Teresa",
    ],
    "Edad": [
        23,
        35,
        np.nan,
        28,
        42,
        36,
        24,
        np.nan,
        30,
        27,
        45,
        22,
        33,
        31,
        np.nan,
        29,
        40,
        26,
        38,
        34,
    ],
    "Ciudad": [
        "Madrid",
        "Barcelona",
        np.nan,
        "Valencia",
        "Sevilla",
        "Zaragoza",
        "Málaga",
        "Murcia",
        "Palma",
        "Las Palmas",
        "Bilbao",
        "Alicante",
        "Córdoba",
        "Valladolid",
        "Vigo",
        "Gijón",
        "Hospitalet",
        "La Coruña",
        "Granada",
        "Elche",
    ],
    "Salario": [
        np.nan,
        32000,
        45000,
        38000,
        30000,
        33000,
        39000,
        41000,
        29000,
        31000,
        47000,
        28000,
        34000,
        np.nan,
        36000,
        37000,
        43000,
        35000,
        44000,
        np.nan,
    ],
}

df_data = pd.DataFrame(data)
df_copy_data = df_data.copy()
# imputacion de datos 

df_fill = df_copy_data.fillna(
    {
    "Edad": df_copy_data["Edad"].mean(),
    "Ciudad": df_copy_data["Ciudad"].mode()[0],  # mode() - es necesario indicar el index
    "Salario": df_copy_data["Salario"].median()
    }
)


""" Interpolacion de valores numericos "Salario" """ 
# En este caso el primer y ultimo dato de mi columna es misssing value hay 3 posibles soluciones 
# 1 - usar metodo Usar un método de interpolación que no dependa de valores anteriores 
df_copy_interpolacion_1 = df_data.copy()
df_copy_interpolacion_1["Salario"] = df_copy_interpolacion_1["Salario"].interpolate(method="bfill")

# 2 - Establecer el valor anetes de interpolar "Salario"
df_copy_interpolacion_2 = df_data.copy()
df_copy_interpolacion_2["Salario"].iloc[0] = df_copy_interpolacion_2["Salario"].mean()
# definimos el valor que nos interesa , con la media 
df_copy_interpolacion_2["Salario"] = df_copy_interpolacion_2["Salario"].interpolate()
# interpolamos los datos restantes 

# 3 - Combinar metodos de interpolacion "Salario"
df_copy_interpolacion_3 = df_data.copy()
df_copy_interpolacion_3["Salario"] = df_copy_interpolacion_3["Salario"].fillna(method="bfill")
df_copy_interpolacion_3["Salario"] = df_copy_interpolacion_3["Salario"].interpolate()

""" Iterpolar valores Str - .mode() """
# Interpolar valores str es diferente - asi que lo hacemos por medio del valor mas constante o definiendo un valor constante 

#df_copy_interpolacion_3["Ciudad"] = df_copy_interpolacion_3["Ciudad"].fillna("N/a")

df_copy_interpolacion_3["Ciudad"] = df_copy_interpolacion_3["Ciudad"].fillna(df_copy_interpolacion_3["Ciudad"].mode()[0])

# Interpolamos la Columna "Edad"
df_copy_interpolacion_3["Edad"] = df_copy_interpolacion_3["Edad"].interpolate()

print("Dataframe 1 - original")
print(df_data)
print("*"*40)
print("DataFrame 1 - Interpolado")
print(df_copy_interpolacion_3)
print("*"*40)
"""
Crea un DataFrame con filas duplicadas y utiliza el m√©todo drop_duplicates() para eliminar esas filas duplicadas.
"""
data_2 = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'John', 'Anna'],
    'Age': [28, 23, 34, 29, 28, 23],
    'City': ['New York', 'Paris', 'London', 'Berlin', 'New York', 'Paris']
}

df_2 = pd.DataFrame(data_2)
df_2_copy = df_2.copy(deep=True)

df_sin_duplicados = df_2_copy.drop_duplicates()  # ELiminacion de filas duplicadas

print("DataFrame 2 - original")
print(df_2_copy)
print("*"*40)
print("DataFrame 2 - Sin filas duplicadas")
print(df_sin_duplicados)


"""
Renombrar columnas:
Crea un DataFrame y renombra las columnas segunn un nuevo conjunto de nombres.
Ordenamiento de columnas:
"""

df_2_copy_renombrado = df_sin_duplicados.rename(columns={"Name": "Nombre", "Age":"Edad", "City":"Ciudad"})
print("*"*40)
print("DataFrame 2 - Renombrado")
print(df_2_copy_renombrado)

"""
Crea un DataFrame y cambia el orden de las columnas utilizando diferentes m√©todos, como la indexaci√≥n o el m√©todo reindex().
"""

df_orden_diferente = ["Nombre", "Ciudad","Edad"]
df_2_nuevo_orden = df_2_copy_renombrado[df_orden_diferente]
print("*"*40)
print("DataFrame 2 - Nuevo Orden")
print(df_2_nuevo_orden)


"""
Transformaci√≥n de datos:
Crea una funci√≥n personalizada y apl√≠cala a una columna existente en un DataFrame para generar una nueva columna con datos transformados.
"""

def mayusculas(palabras:str):
    palabra_nueva = palabras.upper()
    return palabra_nueva 

df_2_nuevo_orden.loc[:, "Nombre_mayus"] = df_2_nuevo_orden["Nombre"].apply(mayusculas)
print(df_2_nuevo_orden)

