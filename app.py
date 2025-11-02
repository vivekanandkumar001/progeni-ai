from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config.from_object("config")

db = SQLAlchemy(app)

# Import routes
from routes import main, auth, resume, interview, notify
app.register_blueprint(main.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(resume.bp)
app.register_blueprint(interview.bp)
app.register_blueprint(notify.bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
