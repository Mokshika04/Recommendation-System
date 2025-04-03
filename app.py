import gradio as gr
import pandas as pd

# Load movie dataset
movies = pd.read_csv("movies.csv") 

# Function to recommend movies by genre
def recommend_by_genre(genre, top_n=5):
    genre_movies = movies[movies["genres"].str.contains(genre, case=False, na=False)]
    if genre_movies.empty:
        return "Genre not found. Please enter a valid genre."
    return "\n".join(genre_movies.sample(n=min(top_n, len(genre_movies)))["title"].tolist())

# Extract unique genres
unique_genres = sorted(set("|".join(movies["genres"]).split("|")))

# Gradio Interface
interface = gr.Interface(
    fn=recommend_by_genre,
    inputs=gr.Dropdown(choices=unique_genres, label="Select a Genre"),
    outputs="text",
    title="🎬 Movie Recommendation System",
    description="Pick a genre to get movie recommendations!"
)

# Launch app
interface.launch()
