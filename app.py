from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import emotion_detection
import os

# Load environment variables
load_dotenv()

app = FastAPI()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

class TextInput(BaseModel):
    text: str

@app.post("/generate-playlist")
def generate_playlist(input: TextInput):
    emotion = emotion_detection.get_emotion(input.text)
    
    emotion_to_playlist = {
        "joy": "happy hits",
        "happy": "happy hits",
        "sadness": "sad songs",
        "bad": "sad songs",
        "down": "sad songs",
        "anger": "rage beats",
        "fear": "relax & unwind",
        "surprise": "party hits",
        "disgust": "chill hits",
        "anticipation": "upbeat vibes",
        "trust": "inspirational tracks",
        "boredom": "mellow moods",
        "contentment": "feel-good tunes",
        "love": "romantic ballads",
        "romance": "romantic ballads",
        "envy": "motivational anthems",
        "frustration": "gritty rock",
        "nostalgia": "throwback classics",
        "hope": "uplifting melodies",
        "curiosity": "exploratory sounds",
        "excitement": "high-energy beats",
        "confusion": "abstract soundscapes",
        "pride": "victory songs",
        "loneliness": "solitude tracks",
        "random": "random tracks"
    }
    
    if emotion.lower() not in emotion_to_playlist:
        raise HTTPException(status_code=400, detail="Emotion not recognized.")
    
    results = sp.search(q=emotion_to_playlist[emotion.lower()], type="playlist", limit=1)
    
    if not results['playlists']['items']:
        raise HTTPException(status_code=404, detail="No playlist found.")
    
    playlist = results['playlists']['items'][0]
    playlist_id = playlist['id']
    playlist_name = playlist['name']
    playlist_description = playlist.get('description', 'No description available')
    
    return {
        "emotion": emotion,
        "playlist_name": playlist_name,
        "playlist_description": playlist_description,
        "playlist_url": f"https://open.spotify.com/playlist/{playlist_id}"
    }

@app.get("/")
def read_root():
    return {"message": "Emotion-Triggered Music Player is running!"}

# Add this block to run the server using Python directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)