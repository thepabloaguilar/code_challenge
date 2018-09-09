from flask import Flask
from flasgger import Swagger

from api import service_a, service_b, service_c

def create_app():
    app = Flask(__name__)

    app.register_blueprint(service_a.api_bp,
                    url_prefix=f'/service-a/v{service_a.SERVICE_A_VERSION}')
    app.register_blueprint(service_b.api_bp,
                    url_prefix=f'/service-b/v{service_b.SERVICE_B_VERSION}')
    app.register_blueprint(service_c.api_bp,
                    url_prefix=f'/service-c/v{service_c.SERVICE_C_VERSION}')

    app.config['SWAGGER'] = {
        'uiversion': 3,
        'swagger_version': '3.0',
        'title': 'Code Challeng API',
        'specs_route': '/challenge-api-docs/',
        'description': 'Documentação para as rotas dos "serviços"',
    }

    swagger = Swagger(app)

    return app
