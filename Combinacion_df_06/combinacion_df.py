import pandas as pd 

data = {
    "Nombre": ["Juan", "Ana", "Luis", "Laura", "Pedro", "Carla"],
    "Ciudad": ["Madrid", "Barcelona", "Madrid", "Valencia", "Barcelona", "Madrid"],
    "Edad": [25, 33, 30, 28, 45, 39],
    "Puntuacion": [80, 90, 85, 88, 75, 91]
}

data_adicional = {
    "Estatura (cm)": [170, 165, 180, 155, 175, 160],
    "Peso (kg)": [70, 60, 85, 50, 75, 55],
    "Genero": ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino"]
}

df_data = pd.DataFrame(data)
df_data_adicional = pd.DataFrame(data_adicional)

df_combinado = pd.concat([df_data,df_data_adicional], ignore_index=True)

print(df_combinado)

