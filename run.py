import os

from app import create_app

config_name = os.getenv('FLASK_ENV')
app = create_app("development")

if __name__ == 'main':
    app.run()