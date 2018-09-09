from flask_restful import Resource
from flasgger import swag_from

from ..model import PostgresSession
from ..model.debt import Debt
from ..model.business import Business

from ..security import auth_token_required
from ..utils import _json_result


# Classe base para as rotas de 'Debt'
class _DebtBase(Resource):

    # Query para pegar as informações de um ou mais Clientes
    def _get_debts_query(self, session, debt_id=None):
        qs = session.query(
            Debt._id.label('idDivida'),
            Debt.customer_id.label('idCliente'),
            Debt.description.label('descricao'),
            Debt.amount.label('valor'),
            Debt.payment_date.label('dataPagamento'),
            Debt.expiry_date.label('dataVencimento'),
            Debt.business_id.label('idEmpresa'),
            Business.business_name.label('nomeEmpresa')
        ).select_from(Debt). \
        join(Business, Business._id == Debt.business_id)

        if debt_id:
            qs = qs.filter(Debt._id == debt_id)
        return qs


class DebtListResource(_DebtBase):

    # Pega todos as dividas e retorna uma lista
    def _get_debts(self):
        session = PostgresSession()
        debts = self._get_debts_query(session)

        try:
            debts = [item._asdict() for item in debts]
        except Exception as e:
            session.close()
            raise e
        finally:
            session.close()
        
        return debts

    @auth_token_required
    @swag_from('../docs/debt/debt_list.yml')
    def get(self):
        return {'debts': _json_result(self._get_debts())}, 200


class DebtResource(_DebtBase):

    # Pega uma divida em especifico
    def _get_debt(self, debt_id):
        session = PostgresSession()
        debt = self._get_debts_query(session, debt_id)

        try:
            debt = debt.one_or_none()._asdict()
        except Exception as e:
            session.close()
            raise e
        finally:
            session.close()
        return debt

    @auth_token_required
    @swag_from('../docs/debt/debt.yml')
    def get(self, debt_id):
        return _json_result(self._get_debt(debt_id)), 200
