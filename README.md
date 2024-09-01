### Setup Instructions

1. Clone the Repository  
clone the repository containing project:  
bash  
git clone https://github.com/parag7923/emotion-music-player 
 
2. Create a Virtual Environment  
bash  
python -m venv venv  

4. Install Dependencies  
bash  
pip install -r requirements.txt  

5. Configure Environment Variables  
Create a .env file in the root directory of the project with the following content:  
env  
SPOTIPY_CLIENT_ID=your_spotify_client_id  
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret  

6. Run the Application  
bash  
python app.py  

7. Access the Application  
Open your web browser and navigate to:  
http://127.0.0.1:8000  

You can also test the API endpoint using curl or Postman:  
Example curl command to test the /generate-playlist endpoint:  
curl -X POST "http://127.0.0.1:8000/generate-playlist"   -H "Content-Type: application/json" -d ’{"text":"I am feeling very happy today!"}’
