import pandas as pd 
import numpy as np 

""" tratamiento de datos - missing values en un df """

data = {
    "nombres": ["ana", "joan", "marta", "jorge"],
    "edad": [12, 12, np.nan, 43],
    "ciudad": ["cdmx", "sonora", None, "madrid"],
}

df = pd.DataFrame(data)

""" ******* imputacion de datos ******* """
# Tratar los datos vacios con "imputacion de datos" - rellenar los datos con por ejemplo, la media, la mediana o la moda de la columna 

df_fill = df.fillna(
    # df.fillna() - metodo para rellener los valores de un DataFrame
    {
    "edad" : df["edad"].mean(),
    # seran rellenados con la media de los datos de esa columna
    "ciudad" : "desconocido"
    }
)

""" ******* Eliminacion condicional ******* """
# eliminar las columnas o filas con valores faltantes 

df_sin_nan = df.dropna()
# metodo para eliminar filas o columas con datos faltantes

# Remplzar datos esecificos de alguna columnna 
df_replace = df.replace(
    # con este metodo indicamos especificamente el item a Remplzar
    {
        "ciudad": {"sonora":"sonora2", None:"desconocidoo"}
    }
)

""" ******* Interpolar valores ****** """

df_interpolado = df.copy()

#df_interpolado["interpolada"] = df["edad"].interpolate()
# en este caso se crea una una col al df llamada "interpolada"

df_interpolado["edad"] = df["edad"].interpolate()
# rellena los missing values  , de con valores estimados basados en los valores existentes en la columna.

""" ******* Tratamiento de datos duplicados ***** """

data_dos = {
    "nombres": ["ana", "joan", "marta", "jorge", "marta"],
    "edad": [12, 12, 22, np.nan, 22],
    "ciudad": ["cdmx", "sonora", "mexico", None, "mexico"],
}

df_ejemplo_dos = pd.DataFrame(data_dos)
df_sin_duplicados = df_ejemplo_dos.drop_duplicates()
df_copy_2 = df_ejemplo_dos.copy()
# para eliminar filas duplicadas en un df

""" ***** Renombrar columnas ****"""
df_renombrando = df.rename(columns={"nombre": "Name", "edad": "Age", "ciudad": "City"})
# rename(), lo que haces es renombrear


""" ****** Ordenamiento de columnas ***** """
# Metodo 1
columnas_orden_1 =["ciudad", "edad", "nombres"] # creamos una lista con el orden que deseamos
df_ordenado = df_ejemplo_dos[columnas_orden_1]  #

# Metodo 2 - .reindex()
columna_orden_2 = ["nombres", "ciudad", "edad"]
df_ordenado_2 = df_ejemplo_dos.reindex(columns=columna_orden_2)
print(df_ordenado_2)

""" ***** Transformacion de datos ***** """
def cuadrado(numero):
    return numero ** 2

df_copy_2["edad cuadrado"] = df_copy_2["edad"].apply(cuadrado)
print(df_copy_2)

# generamos una columna mas donde aplicamos la funcion cuadradoo a cada dato de edad


