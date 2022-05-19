from flask import Flask
from config import config


# Routes
from routes import list_route_for_app

app = Flask(__name__)

# Error 404 
def page_not_found(error):
    return "<h1> Not found page <h1>", 404
    
if __name__ == '__main__':
    
    #Config app
    app.config.from_object(config['development'])
    
    # Blueprints
    app.register_blueprint(list_route_for_app.main, url_prefix='/api/')
    
    # Error handlers 
    app.register_error_handler(404, page_not_found)
    
    # # Run app development
    # app.run()
    
     # Run app production
    app.run(host='0.0.0.0', port=8000)
    
  