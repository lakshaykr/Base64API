from flask import Flask, redirect, url_for
import os
from werkzeug.routing import BuildError  

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") or os.urandom(24).hex()
if not app.config['SECRET_KEY']:
    raise RuntimeError("SECRET_KEY not set and failed to generate a fallback")

with app.app_context():
    from dashboard import bp as dashboard_bp  
    from main import bp as api_bp

app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def home():
    try:
        return redirect(url_for('dashboard.home'))  
    except BuildError as e:
        app.logger.error(f"Redirect failed: {str(e)}")
        return redirect('/dashboard')  # Fallback

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
    app.run(host='0.0.0.0', port=5000)