import pandas as pd

# creacion de una serie en pd - es un dato unidimensional
numeros = [1, 2, 3, 4, 5]
serie = pd.Series(numeros)
print(type(serie))

# Creacion de un dataframe - es un dato bidimensional

data = {
    "nombres": ["ana", "joan", "marta", "jorge"],
    "edad": [12, 12, 32, 43],
    "ciudad": ["cdmx", "sonora", "puebla", "madrid"],
}

data_frame = pd.DataFrame(data)  # creacion dataframe
print(data_frame)

# exportar un data_frame
data_frame.to_csv("data.csv")

# importar un dataframe
import_df = pd.read_csv("data.csv", index_col=0)
# index_col = - lo que hace es eliminar la col de index que pd genera 
print(import_df)

""" seleccion de columnas """
columna_nombres = data_frame["nombres"]
columnas_seleccion = data_frame[["nombres", "edad"]]


""" Seleccionamos filas """
fila_seleccionada = data_frame.loc[1] 
# filtrar por filas y columnas basadas en etiquetas

""" Maneras de filtrar los datos  """
# filtramos por 1  - condicion 
filtrar_fila_condicion = data_frame[data_frame["edad"] > 30]

# filtras por 2 - condiciones 
filtro_condiciones = (data_frame["edad"] > 30) & (data_frame["nombres"].str.startswith("m"))
print(data_frame[filtro_condiciones])

# filtrar por query - que es para filtrar por una condicion
filtrar_query = data_frame.query("edad > 10 ")

# Metodos para reaalizar filtraciones mas especificas 
# en este metodo filtrar si esta dentro de 
filtrar_isin = data_frame[data_frame["nombres"].isin(["jorge", "carllos"])]

# filtrar por funciones
def longitud_5(nombre):
    return len(nombre) == 5 

filtrado_por_fucion = data_frame[data_frame["nombres"].apply(longitud_5)]
# se especifica la colunna , y se llama a la funcioin .apply - donde en cada fila se ejecutara la fucnion declarada 

# filtrar entre rangos .between
filtrar_por_rango = data_frame[data_frame["edad"].between(20, 50)]
print("*"*40)

