
import pandas as pd

"""
AGRUPACION DE DATOS
"""

# groupby() - Te permite agrupar tus datos en base a una o más columna

data = {
    "Nombre": ["Juan", "Ana", "Luis", "Laura", "Pedro", "Carla"],
    "Ciudad": ["Madrid", "Barcelona", "Madrid", "Valencia", "Barcelona", "Madrid"],
    "Edad": [25, 33, 30, 28, 45, 39],
    "Puntuacion": [80, 90, 85, 88, 75, 91]
}

df = pd.DataFrame(data)

# Agrupacion de datos por ciudad 
grouped = df.groupby("Nombre")

# Genera los grupos de manera desordenada 
print(grouped.groups)

# mostramos los grupos generados 
for nombre, grupo in grouped:
    print("\n", nombre)
    print(grupo)


