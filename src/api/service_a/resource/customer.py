from flask import abort
from flask_restful import Resource
from flasgger import swag_from

from ..model import PostgresSession
from ..model.customer import Customer
from ..model.debt import Debt
from ..model.business import Business

from ..security import auth_token_required
from ..utils import _json_result


# Classe base para as rotas de 'Customer'
class _CustomerBase(Resource):

    # Retorna a Query para pegar as informações dos Clientes no Banco
    def _get_customers_query(self, session, tax_id=None):
        session = PostgresSession()

        qs = session.query(
            Customer._id.label('id'),
            Customer.tax_id.label('cpf'),
            Customer.customer_name.label('nome'),
            Customer.customer_address.label('endereco')
        ).select_from(Customer)

        if tax_id:
            qs = qs.filter(Customer.tax_id == tax_id)
        return qs

    # Retorna a Query para pegar as informações das Dividas no Banco
    def _get_debts_query(self, session, tax_id=None):
        qs = session.query(
            Debt.customer_id.label('idCliente'),
            Debt.business_id.label('idEmpresa'),
            Business.business_name.label('nomeEmpresa'),
            Debt.amount.label('valor'),
            Debt.description.label('descricao'),
            Debt.payment_date.label('dataPagamento'),
            Debt.expiry_date.label('dataVencimento')
        ).select_from(Debt). \
        join(Business, Business._id == Debt.business_id)

        if tax_id:
            qs = qs.join(Customer, Customer._id == Debt.customer_id). \
                filter(Customer.tax_id == tax_id)
        return qs


class CustomerListResource(_CustomerBase):
    
    # Filtra a lista de dividas pelo id do Cliente
    # Posteriormente coloca a lista de dividas para o Cliente
    def _format_informations(self, customers, debts):
        customers = [item._asdict() for item in customers]
        debts = [item._asdict() for item in debts]
        
        for customer in customers:
            _filter = lambda x: x['idCliente'] == customer['id']
            customer['dividas'] = list(filter(_filter, debts))
        return customers
    
    # Pega as informações e as devolve formatadas
    def _get_informations(self):
        session = PostgresSession()
        customers = self._get_customers_query(session)
        debts = self._get_debts_query(session)
        try:
            result = self._format_informations(customers, debts)
        except Exception as e:
            session.close()
            raise e
        finally:
            session.close()
        return result

    @auth_token_required
    @swag_from('../docs/customer/customer_list.yml')
    def get(self):
        return {'customers': _json_result(self._get_informations())}, 200


class CustomerResource(_CustomerBase):

    # Coloca a lista de dividas para o Cliente filtrado
    def _format_informations(self, customer, debts):
        customer['dividas'] = [item._asdict() for item in debts]
        return customer

    # Pega as informações de um Cliente que foi filtrado
    def _get_informations(self, tax_id):
        session = PostgresSession()

        customer = self._get_customers_query(session, tax_id)

        try:
            customer = customer.one_or_none()
            if not customer:
                abort(404, 'Cliente não encontrado')
            customer = customer._asdict()
            debts = self._get_debts_query(session, tax_id)
            result = self._format_informations(customer, debts)
        except Exception as e:
            session.close()
            raise e
        finally:
            session.close()
        return result

    @auth_token_required
    @swag_from('../docs/customer/customer.yml')
    def get(self, tax_id):
        return _json_result(self._get_informations(tax_id)), 200
