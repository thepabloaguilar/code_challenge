import flask_restful

from flask import Blueprint
from .resource import customer, debt, login

api_bp = Blueprint('service_a', __name__)
api = flask_restful.Api(api_bp)

SERVICE_A_VERSION = 1

api.add_resource(customer.CustomerListResource, '/customer')
api.add_resource(customer.CustomerResource, '/customer/<tax_id>')

api.add_resource(debt.DebtListResource, '/debt')
api.add_resource(debt.DebtResource, '/debt/<debt_id>')

api.add_resource(login.Login, '/login')
