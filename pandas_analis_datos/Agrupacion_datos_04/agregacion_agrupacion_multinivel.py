import pandas as pd 

"""
AGREGACION Y AGRUPACION MILTINIVEL
"""

data = {
    "Nombre": ["Juan", "Ana", "Luis", "Laura", "Pedro", "Carla"],
    "Ciudad": ["Madrid", "Barcelona", "Madrid", "Valencia", "Barcelona", "Madrid"],
    "Edad": [25, 33, 30, 28, 45, 39],
    "Puntuacion": [80, 90, 85, 88, 75, 91]
}

data["Categoria"] = ["A", "B", "A", "B", "A", "B"]
df = pd.DataFrame(data)
print(df)

#  Agrupar datos por ciudad y Categoria

grouped_multi = df.groupby(["Ciudad", "Categoria"])
print("*"*41)
print(grouped_multi.groups)

