from flask import Flask
from routes.main import main_bp
from routes.auth import auth_bp
from routes.resume import resume_bp
from routes.interview import interview_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(resume_bp)
app.register_blueprint(interview_bp)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)
