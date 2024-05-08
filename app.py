from fastapi import FastAPI
from typing import List
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder

# Carga de los datasets
items_game = pd.read_csv('Datacsv/items_games_.csv', parse_dates=['Release_date'])
review_game = pd.read_csv('Datacsv/review_games_.csv', parse_dates=['Release_date', 'Posted'])

app = FastAPI()

# Función para encontrar el año de lanzamiento con más horas jugadas para un género dado
def PlayTimeGenre(genero):
    juegos_genero = items_game[items_game['Genres'].str.contains(genero, case=False)]
    horas_por_año = juegos_genero.groupby(juegos_genero['Release_date'].dt.year)['Playtime_forever'].sum()
    año_mas_horas = horas_por_año.idxmax()
    return {"Año de lanzamiento con más horas jugadas para " + genero: int(año_mas_horas)}

# Función para encontrar el usuario con más horas jugadas para un género dado
def UserForGenre(genero):
    juegos_genero = items_game[items_game['Genres'].str.contains(genero, case=False)]
    if juegos_genero.empty:
        return "No se encontraron juegos para el género especificado."
    horas_por_usuario_y_año = juegos_genero.groupby(['User_id', juegos_genero['Release_date'].dt.year])['Playtime_forever'].sum()
    usuario_mas_horas = horas_por_usuario_y_año.groupby(level=0).sum().idxmax()
    horas_por_año_usuario = horas_por_usuario_y_año.loc[usuario_mas_horas].reset_index()
    horas_por_año_usuario.rename(columns={'Release_date': 'Año', 'Playtime_forever': 'Horas'}, inplace=True)
    horas_por_año_usuario = horas_por_año_usuario.to_dict(orient='records')
    return {"Usuario con más horas jugadas para " + genero: usuario_mas_horas, "Horas jugadas": horas_por_año_usuario}

# Función para obtener los juegos más recomendados para un año dado
def UsersRecommend(año: int):
    reseñas_año = review_game[review_game['Posted'].dt.year == año]
    reseñas_recomendadas = reseñas_año[reseñas_año['Recommend']]
    juegos_recomendados = reseñas_recomendadas['App_name'].value_counts()
    top_3_juegos = juegos_recomendados.head(3)
    return [{"Puesto {}".format(index + 1): juego} for index, juego in enumerate(top_3_juegos.index)]

# Función para obtener los juegos menos recomendados para un año dado
def UsersNotRecommend(año: int):
    reseñas_año = review_game[review_game['Posted'].dt.year == año]
    reseñas_no_recomendadas = reseñas_año[~reseñas_año['Recommend']]
    juegos_no_recomendados = reseñas_no_recomendadas['App_name'].value_counts()
    top_3_juegos = juegos_no_recomendados.head(3)
    return [{"Puesto {}".format(index + 1): juego} for index, juego in enumerate(top_3_juegos.index)]

# Función para realizar un análisis de sentimiento para un año dado
def sentiment_analysis(año: int):
    reseñas_año = review_game[review_game['Posted'].dt.year == año]
    count_sentiments = reseñas_año['Sentiment_analysis'].value_counts()
    resultado = {"Positive": count_sentiments.get(2, 0),
                 "Neutral": count_sentiments.get(1, 0),
                 "Negative": count_sentiments.get(0, 0)}
    return resultado


# Función para recomendar juegos similares a uno dado
def recomendacion_juego(id_producto: int):
    juegos_rel = review_game[review_game['Id'] == id_producto]
    juegos_rel = juegos_rel.drop(columns=['Id', 'App_name', 'User_id', 'Posted', 'Release_date'])
    encoder_genres = LabelEncoder()
    juegos_rel['Genres'] = encoder_genres.fit_transform(juegos_rel['Genres'])
    juegos_rel['Recommend'] = juegos_rel['Recommend'].astype(int)
    matriz_similitud = cosine_similarity(juegos_rel)
    juegos_similares_indices = matriz_similitud.argsort()[0][-6:-1][::-1]
    juegos_similares = review_game.loc[juegos_similares_indices, 'App_name'].tolist()
    return juegos_similares

 # Función para recomendar juegos similares según el usuario
def recommendation_user(user_id: str):
    juegos_rel = review_game[review_game['User_id'] == user_id]
    juegos_rel = juegos_rel.drop(columns=['Id', 'App_name', 'User_id', 'Posted', 'Release_date', 'Recommend', 'Sentiment_analysis'])
    encoder_genres = LabelEncoder()
    juegos_rel['Genres'] = encoder_genres.fit_transform(juegos_rel['Genres'])
    matriz_similitud = cosine_similarity(juegos_rel)
    juegos_similares_indices = matriz_similitud.argsort()[0][-6:-1][::-1]
    juegos_similares = review_game.loc[juegos_similares_indices, 'App_name'].tolist()
    return {"recommended_games": juegos_similares}


@app.get("/playtime_genre/{genre}")
async def get_playtime_genre(genre: str):
    return PlayTimeGenre(genre)

@app.get("/user_for_genre/{genre}")
async def get_user_for_genre(genre: str):
    return UserForGenre(genre)

@app.get("/users_recommend/{year}")
async def get_users_recommend(year: int):
    return UsersRecommend(year)

@app.get("/users_not_recommend/{year}")
async def get_users_not_recommend(year: int):
    return UsersNotRecommend(year)

@app.get("/sentiment_analysis/{year}")
async def get_sentiment_analysis(year: int):
    return sentiment_analysis(year)

@app.get("/recommendation_game/{product_id}")
async def get_recommendation_game(product_id: int):
    return recomendacion_juego(product_id)

@app.get("/recommendation/{user_id}")
async def get_recommendation(user_id: str):
    return recommendation_user(user_id)
