import os

from flask import abort
from flask_restful import Resource
from flasgger import swag_from

from ..database import get_mongo_client


class CustomerListResource(Resource):

    # Pega todos os documentos salvos na collection, 'customer'
    def _get_customers(self):
        client = get_mongo_client('customer')
        cursor = client.find({}, {'_id': 0,})
        customers = [item for item in cursor]
        cursor.close()
        return customers

    @swag_from('../docs/customer/customer_list.yml')
    def get(self):
        return {'customers': self._get_customers()}, 200


class CustomerResource(Resource):

    # Pega um documento especifico filtrado pelo cpf,
    # o mesmo salvo na collection, 'customer'
    def _get_customer(self, tax_id):
        client = get_mongo_client('customer')
        customer = client.find_one({'cpf': tax_id}, {'_id': 0,})
        if not customer:
            abort(404, 'Cliente não encontrado')
        return customer

    @swag_from('../docs/customer/customer.yml')
    def get(self, tax_id):
        return self._get_customer(tax_id), 200
