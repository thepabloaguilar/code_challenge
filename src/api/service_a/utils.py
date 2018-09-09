import os
import json

from datetime import date
from decimal import Decimal


# Converte objetos não Serializaveis para objetos Serializaveis
def _json_encoder(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')


# Formata o dicionario de retorno para dar o retorno da request
def _json_result(result):
    return json.loads(json.dumps(result, default=_json_encoder))
