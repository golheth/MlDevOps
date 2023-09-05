import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os




df_combined = pd.read_parquet('df_combined.parquet')

df_combined = df_combined.reset_index(drop=True)







categories = df_combined[['web_publishing', 'audio_production', 'strategy', 'adventure', 'photo_editing', 'rpg', 'action', 'utilities', 'accounting', 'free_to_play', 'massively_multiplayer', 'education', 'software_training', 'animation_modeling', 'racing', 'casual', 'design_illustration', 'early_access', 'simulation', 'sports', 'indie', 'video_production']]

# Calcula la matriz de similitud del coseno entre los juegos en función de las categorías
similarity_matrix = cosine_similarity(categories, categories)

# Función para obtener recomendaciones para un juego específico
def get_recommendations(game_name, similarity_matrix, num_recommendations=5):
    game_index = df_combined[df_combined['game'] == game_name].index[0]
    game_similarity = similarity_matrix[game_index]
    game_indices = game_similarity.argsort()[::-1]  # Ordenar por similitud descendente
    recommendations = []

    for i in range(1, num_recommendations + 1):
        recommended_game_index = game_indices[i]
        recommended_game_name = df_combined.loc[recommended_game_index, 'game']
        recommendations.append(recommended_game_name)

    return recommendations

# Obtener recomendaciones para un juego específico (reemplace 'NombreDelJuego' con el juego que desees)
game_name_to_recommend = 'ironbound'
num_recommendations = 5
recommendations = get_recommendations(game_name_to_recommend, similarity_matrix, num_recommendations)

print(f"Recomendaciones para el juego {game_name_to_recommend}:")
for i, recommended_game_name in enumerate(recommendations):
    print(f"{i + 1}: {recommended_game_name}")
