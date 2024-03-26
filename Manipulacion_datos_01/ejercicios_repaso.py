"""
Ejercicios repaso de manipulacion de datos
"""
import pandas as pd 


# Configura pandas para mostrar todas las columnas
pd.set_option('display.max_columns', None)

# Configura pandas para mostrar todas las filas
pd.set_option('display.max_rows', None)



def separacion():
    print("*"*80)


"""
Creación de DataFrame y Series:
Crea una Serie que contenga tus cinco números favoritos y muéstrala por pantalla.
Crea un DataFrame que contenga información sobre tus películas favoritas, con columnas para el título, el género y el año de lanzamiento.
"""
# ejercicio 1 
# Genera serie
numeros_favoritos = ["1","6","10"]
favoritos_serie = pd.Series(numeros_favoritos)
print(favoritos_serie)
separacion()
 
# Genera DataFrame 
peliculas = {
    "titulo": [
        "Titanic",
        "Jurassic Park",
        "Avatar",
        "The Shawshank Redemption",
        "Inception",
        "The Godfather",
        "The Dark Knight",
        "Forrest Gump",
        "Schindler's List",
        "The Matrix"
    ],
    "genero": [
        "Drama",
        "Aventura",
        "Ciencia ficción",
        "Drama",
        "Ciencia ficción",
        "Drama",
        "Acción",
        "Drama",
        "Drama",
        "Ciencia ficción"
    ],
    "lanzamiento": [
        1997,
        1993,
        2009,
        1994,
        2010,
        1972,
        2008,
        1994,
        1993,
        1999
    ]
}
df_peliculas = pd.DataFrame(peliculas)
print(df_peliculas)
separacion()

"""
Exportación e importación de datos:
Exporta tu DataFrame de películas favoritas a un archivo CSV y luego vuelve a importarlo.
Exporta tu Serie de números favoritos a un archivo de texto y luego vuelve a importarlo.
"""

# Exportación de df
df_peliculas.to_csv("peliculas")

# Importacion de df
import_df = pd.read_csv("peliculas", index_col=0)
print("DataFrame IMPORTADO")
print(import_df)
separacion()

"""
Selección de datos:
Selecciona la tercera fila de tu DataFrame de películas favoritas.
Selecciona la columna de género de tu DataFrame de películas favoritas.
Selecciona las primeras tres filas de tu DataFrame de películas favoritas.
"""

# seleccionamos la 3era fila
df_tercera_fila = df_peliculas.loc[2]
print(df_tercera_fila)
separacion()

# seleccion de columnas 
df_seleecion_genero = df_peliculas["genero"]
print(df_seleecion_genero)
separacion()

# seleccion de 3 filas
df_seleccio_3 = df_peliculas.loc[0:2]
print(df_seleccio_3)
separacion()

"""
Filtrado de datos:
Filtra las películas de tu DataFrame favorito que se lanzaron después del año 2000.
Filtra las películas de tu DataFrame favorito que sean del género "Acción".
Filtra las películas de tu DataFrame favorito que sean del género "Comedia" y se lanzaron después del año 2010
"""

# filtrar por años las peliculas 
df_filtro_año = df_peliculas[df_peliculas["lanzamiento"] > 2000]
print(df_filtro_año)
separacion()

# filtramos por genero de Acción 
df_filtro_accion = df_peliculas[df_peliculas["genero"].isin(["Acción"])]
print(df_filtro_accion)
separacion()


# filtro de comedia y 2010 
 # mal ---- df_filtro_comedia_2010 = df_peliculas[df_peliculas["genero"].isin(["Drama"]) & df_peliculas[df_peliculas["lanzamiento"] < 2010]]
df_filtro_comedia_2010 = df_peliculas[(df_peliculas["genero"] == "Drama") & (df_peliculas["lanzamiento"] < 2010)]
print(df_filtro_comedia_2010)
separacion()

"""
Métodos avanzados de filtrado:
Filtra las películas de tu DataFrame favorito que tengan un título que comience con la letra "T".
Filtra las películas de tu DataFrame favorito cuyos títulos sean exactamente cinco caracteres de longitud.
"""
# filtro de titulo - titulos que comiencen con T
df_filtro_letraT = df_peliculas[df_peliculas["titulo"].str.startswith("T")]
print(df_filtro_letraT)
separacion()


# Filyto de len de los titulos
def long(nombre):
    return len(nombre) == 7

df_len_cinco = df_peliculas[df_peliculas["titulo"].apply(long)]
print(df_len_cinco)
separacion()
"""
Filtrado por rangos:
Filtra las películas de tu DataFrame favorito que se lanzaron entre los años 1990 y 2000.
Filtra las películas de tu DataFrame favorito cuyos años de lanzamiento estén fuera del rango de 1980 a 2020.
"""

# filtro del rango 1990 y 2000
df_filtro_rango = df_peliculas[df_peliculas["lanzamiento"].between(1990, 2000)]
print(df_filtro_rango)

# filtro diferente a 1980 a 2020
df_filtro_rango_2 = df_peliculas[-df_peliculas["lanzamiento"].between(1980, 2020)]
print(df_filtro_rango_2)

