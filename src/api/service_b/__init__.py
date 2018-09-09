import flask_restful

from flask import Blueprint
from .resource import customer

api_bp = Blueprint('service_b', __name__)
api = flask_restful.Api(api_bp)

SERVICE_B_VERSION = 1

api.add_resource(customer.CustomerListResource, '/customer')
api.add_resource(customer.CustomerResource, '/customer/<tax_id>')
