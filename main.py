from project.app import create_app, logger
from flask_cors import CORS


logger.info('Server has started.')

app = create_app()

CORS(app)
if __name__ == "__main__":
    app.run()