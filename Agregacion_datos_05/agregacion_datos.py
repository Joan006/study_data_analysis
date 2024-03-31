import pandas as pd 

data = {
    "Nombre": ["Juan", "Ana", "Luis", "Laura", "Pedro", "Carla"],
    "Ciudad": ["Madrid", "Barcelona", "Madrid", "Valencia", "Barcelona", "Madrid"],
    "Edad": [25, 33, 30, 28, 45, 39],
    "Puntuacion": [80, 90, 85, 88, 75, 91]
}

df_data = pd.DataFrame(data)

# Agregar una columna 
df_data["Mes Nacimiento"] = ["Abril", "Mayo", "Dic", "Enero", "Febrero", "Junio"]

# Agregar filas 
new_row = pd.Series({"Nombre": "Pedro", "Edad":45, "Ciudad":"Mex", "Puntuacion": 23})
df_data = pd.concat([df_data, new_row.to_frame().T], ignore_index=True)
print(df_data)

