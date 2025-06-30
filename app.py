from flask import Flask, render_template, request, session, redirect
#from config import TOKEN, CLIENT_SECRET, OAUTH_URL, REDIRECT_URI
from zenora import APIClient


from dotenv import load_dotenv
import os

load_dotenv()  
TOKEN = os.getenv("TOKEN")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
OAUTH_URL = os.getenv("OAUTH_URL")
REDIRECT_URI = os.getenv("REDIRECT_URI")
FLASK_SECRET = os.getenv("SECRET")

app = Flask(__name__)
app.config['SECRET_KEY'] = f"{FLASK_SECRET}"
client = APIClient(TOKEN, client_secret=CLIENT_SECRET)

@app.route('/')
def home():
    if 'token'  in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template("index.html", current_user=current_user)
    return render_template('index.html', oath_uri=OAUTH_URL)

@app.route('/oauth/callback')
def callback():
    code = request.args['code']
    oauth_response = client.oauth.get_access_token(code, REDIRECT_URI)
    access_token = oauth_response.access_token
    session['token'] = access_token
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
