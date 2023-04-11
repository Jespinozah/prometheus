# main.py
from flask import Flask
from flask_cors import CORS
from config import config
#Routes
from routes import customer
from routes import auth 

app = Flask(__name__)
CORS(app)

def page_not_found(error):
    return "<h1>Not Found Page<h1>", 404 
if __name__ == "__main__":
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(customer.main,url_prefix='/api/customers')
    app.register_blueprint(auth.bpAuth)

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
