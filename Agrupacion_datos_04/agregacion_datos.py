import pandas as pd

data = {
    "Nombre": ["Juan", "Ana", "Luis", "Laura", "Pedro", "Carla"],
    "Ciudad": ["Madrid", "Barcelona", "Madrid", "Valencia", "Barcelona", "Madrid"],
    "Edad": [25, 33, 30, 28, 45, 39],
    "Puntuacion": [80, 90, 85, 88, 75, 91]
}

df = pd.DataFrame(data)
# Agrupacion de datos por ciudad 
grouped = df.groupby("Ciudad")
print(grouped.groups)
# Calcular la suma de las edades y Puntuacion por edad 

df_aggregated =grouped.agg(
    {
        "Edad":"mean",
        "Puntuacion": "sum"
    }
)
print("*"*40)
print(df_aggregated)


#  plicar una funcion a un agg de grupo 

def rango(serie):
    return serie.max() - serie.min()


agregacion_data_custom = grouped.agg(
    # Con la funcion agg , a cada item del grupo generado por columna se le aaplica la fucion de rango 
    {
        "Edad": rango,
        "Puntuacion": rango
    }
)
print("*"*40)
print(agregacion_data_custom)
