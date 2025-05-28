from flask import Flask
import os 

app = Flask(__name__)

@app.route('/')
def home():
    return f"Hello from Flask! Connected to DB at {os.getenv('DATABASE_URL')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
