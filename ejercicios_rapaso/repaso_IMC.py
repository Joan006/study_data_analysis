import pandas as pd 
import numpy as np 

pd.set_option('display.max_rows', None)  # Muestra todas las filas
pd.set_option('display.max_columns', None)  # Muestra todas las columnas

"""
Crea un DataFrame con las siguientes columnas: "Nombre", "Edad", "Altura", "Peso".
"""

data = {
    "Nombre": ["Ana", "Luis", "Carlos", "María", "Elena", "Jorge", "Berta", "David", "Sofía", "Ricardo"],
    "Edad": [28, 34, 45, 23, 31, 38, 22, 29, 27, 36],
    "Altura": [1.65, 1.78, 1.72, 1.60, 1.67, 1.82, 1.58, 1.75, 1.64, 1.80],
    "Peso": [55, 78, 108, 54, 91, 73, 79, 107, 58, 35]
}

df = pd.DataFrame(data)
"""
Agrega una nueva columna llamada "IMC" (√çndice de Masa Corporal) calculada como el peso dividido por la altura al cuadrado.
"""
def calculadora_imc(row):
    return row["Peso"] / row["Altura"]**2

df["IMC"] = df.apply(calculadora_imc, axis=1)

"""
Utiliza np.where() para crear una nueva columna llamada "Clasificaci√≥n_IMC" que clasifique el IMC en "Bajo peso", "Peso normal", "Sobrepeso" y "Obesidad", utilizando los siguientes criterios:
IMC < 18.5: "Bajo peso"
18.5 <= IMC < 25: "Peso normal"
25 <= IMC < 30: "Sobrepeso"
IMC >= 30: "Obesidad"
"""
condiciones = [
    (df['IMC'] < 18.5),
    (df['IMC'] >= 18.5) & (df['IMC'] < 25),
    (df['IMC'] >= 25) & (df['IMC'] < 30),
    (df['IMC'] >= 30)
]

clasificacion = ["Bajo peso", "Peso Normal", "Sobrepeso", "Obesidad"]

df["Clasi_IMC"] = np.select(condiciones, clasificacion)

"""
Calcula el promedio de la edad, altura y peso en el DataFrame.
"""

media = df[["Edad", "Altura", "Peso"]].mean()
print("Media de Edad, Altura, Peso")
print(media)
print("*"*40)

"""
Encuentra el nombre de la persona m√°s joven y la m√°s vieja en el DataFrame.
"""

persona_mas_joven = df[["Edad", "Nombre"]].min()
print("La persona mas joven")
print(persona_mas_joven)

persona_mas_adulta = df[["Edad", "Nombre"]].max()
print("La persona mas adulta")
print(persona_mas_adulta)
print("*"*40)

"""
Calcula la suma de la columna "Peso" para aquellos que tienen una edad superior a 30 a√±os.
"""
personas_mas_treinta = df[df["Edad"] > 30].agg(
    {
        "Peso": "sum"
    }
)

print("Suma de columna Peso - personas mayores a 30 años")
print(personas_mas_treinta)
print("*"*40)

"""
Agrupa el DataFrame por la clasificaci√≥n del IMC y calcula el promedio de la edad, altura y peso para cada grupo.
"""

agrupacion_IMC = df.groupby(["IMC"]).agg(
    {
        "Edad":"mean",
        "Altura":"mean",
        "Peso": "mean"
    }
)
print(agrupacion_IMC)
print("*"*40)
"""
Crea una nueva columna que indique si la persona tiene un IMC superior al promedio del IMC en todo el DataFrame.
"""
print(df)
promedio_IMC = df["IMC"].mean()

df["Promedio_IMC"] = np.where(df["IMC"] > promedio_IMC , "promedio", "no-promedio")
print(df)

