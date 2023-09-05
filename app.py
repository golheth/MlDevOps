import uvicorn
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from typing import List


from fastapi import FastAPI
app = FastAPI()



# Importa tus funciones y DataFrames
from Functions import get_game_recommendations



# Define modelos Pydantic para las solicitudes y respuestas
class GameRequest(BaseModel):
    game_name: str



# Carga tus DataFrames

df_combined = pd.read_parquet('df_combined.parquet')


df_combined = df_combined.reset_index(drop=True)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a tu API personalizada"}




@app.post("/recommendations/")
def get_game_recommendations(game_request: GameRequest):
    recommendations = get_recommendations(game_request.game_name, similarity_matrix, num_recommendations)
    return {"recommendations": recommendations}



