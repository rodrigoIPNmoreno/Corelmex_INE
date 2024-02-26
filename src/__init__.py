from flask import Flask

# ---->> routes
from .routes import AuthRoutes
#from .routes import NeuralNetworksRoutes
from .routes import DetectionOCRRoutes
from .routes import AddImagesRoutes
#from .routes import ShowInfo

app = Flask(__name__)

def init_app(config):
    # ---->> configuracione
    app.config.from_object(config)

    # ---->> Blueprints para estructurar en subaplicaciones/modulos pequenhos
    app.register_blueprint(AuthRoutes.main, url_prefix = '/authroutes')
    #app.register_blueprint(NeuralNetworksRoutes.main, url_prefix = '/neuralroutes')
    app.register_blueprint(DetectionOCRRoutes.main, url_prefix = '/detectionroutes')
    app.register_blueprint(AddImagesRoutes.main, url_prefix = '/addimgroutes')
    #app.register_blueprint(ShowInfo.main, url_prefix = '/showinforoutes')

    return app
