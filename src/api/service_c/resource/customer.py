import os

from flask_restful import Resource
from flasgger import swag_from

from ..database import get_elasticsearch_connection


class CustomerListResource(Resource):

    # Pega e retorna todos os Clientes em uma lista
    # com suas respectivas movimentações financeiras
    def _get_customers(self):
        es = get_elasticsearch_connection()

        query = {"query": {"match_all": {}}}
        res = es.search(index='customer', body=query)

        customers = [hit['_source'] for hit in res['hits']['hits']]
        return customers

    @swag_from('../docs/customer/customer_list.yml')
    def get(self):
        return {'customers': self._get_customers()}, 200


class CustomerResource(Resource):

    # Pega um Cliente especifico e devolve suas
    # movimentações financeiras
    def _get_customer(self, tax_id):
        es = get_elasticsearch_connection()

        query = {"query": {"match": {'cpf': tax_id}}}
        res = es.search(index='customer', body=query)
        return res['hits']['hits'][0]['_source']

    @swag_from('../docs/customer/customer.yml')
    def get(self, tax_id):
        return self._get_customer(tax_id), 200
