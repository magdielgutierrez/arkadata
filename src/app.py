from flask import Flask
from config import config
from flask_cors import CORS



# Routes
from routes import list_route_for_app

app = Flask(__name__)
CORS(app, resources={"*":{"origins":"http://localhost:9393"}})

def page_not_found(error):
    return "<h1> Not found page <h1>", 404
    

if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    # Blueprints
    app.register_blueprint(list_route_for_app.main, url_prefix='/api/records')
    
    # Error handlers 
    app.register_error_handler(404, page_not_found)
    app.run()