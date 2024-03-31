"""
Ejercicios de repaso
"""
import pandas as pd

# Crear un nuevo DataFrame
data = {
    "Nombre": ["María", "Carlos", "Elena", "Miguel", "Sofía", "Andrés"],
    "Ciudad": ["Madrid", "Barcelona", "Madrid", "Valencia", "Barcelona", "Madrid"],
    "Edad": [28, 35, 32, 29, 40, 37],
    "Puntuacion": [85, 92, 89, 83, 78, 95],
    "Categoria": ["A", "B", "B", "A", "A", "B"],
}

df_data = pd.DataFrame(data)

# Calcular el promedio de edad y puntuación por categoría.
df_promedio_categoria = df_data.groupby("Categoria").agg(
    {
    "Edad":"mean",
    "Puntuacion": "mean"
    }
)
print("**** Promedio de edad y puntuación por categoría ***** ")
print(df_promedio_categoria)

# Filtrar datos para mostrar solo las personas que tienen una puntuación superior a 30.
df_filtracion_edad = df_data[df_data["Edad"] > 30]
print("***** Filtracion por edad *****")
print(df_filtracion_edad)

# Calcular la suma de las puntuaciones para cada ciudad.
df_suma_puntuaciones = df_data.groupby("Ciudad").agg(
    {
        "Puntuacion":"sum"
    }
)
print("***** Suma de las Puntuaciones por Ciudades *****")
print(df_suma_puntuaciones)

# Ordenar el DataFrame por edad en orden ascendente y puntuación en orden descendente

def ordenacion_ascendente(dato):
    return sorted(dato, reverse=False)

def ordenacion_descendente(datos):
    return sorted(datos, reverse=True)

df_copy = df_data.copy()

# Aplicando orden ascendente a la columna 'Edad'
df_grande_ordenado = df_copy.sort_values(by=["Edad", "Puntuacion"], ascending=[True, False])
print("\n4. DataFrame ordenado por edad ascendente y puntuación descendente:")
print(df_grande_ordenado)


# Contar cuántas personas hay en cada categoría.
df_por_categoria = df_grande_ordenado["Categoria"].value_counts()
print(df_por_categoria)


print("*"*40)
print("DATAFRAME ORIGINAL")
print(df_data)
