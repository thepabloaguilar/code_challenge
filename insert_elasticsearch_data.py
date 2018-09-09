import elasticsearch

from datetime import datetime, timedelta

es = elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200}])

data = [
    {
        'nome': 'Luke Skywalker',
        'cpf': 'f7bc221a-3dca-43b3-bc71-2704e9815fd4',
        'ultimaConsulta': datetime.utcnow(),
        'ultimaCompraCC': {
            'date': datetime.utcnow() - timedelta(days=28),
            'valor': 85365.89
        },
        'movimentacaoFinanceira': [
            {
            "tipo": "cartao-galactico",
            "valor": 85365.89,
            "data": datetime.utcnow() - timedelta(days=28)
            },
            {
            "tipo": "transferencia",
            "valor": 500.00,
            "data": datetime.utcnow() - timedelta(days=29)
            },
            {
            "tipo": "cartao-galactico",
            "valor": 95512.55,
            "data": datetime.utcnow() - timedelta(days=32)
            }
        ]
    },
    {
        'nome': 'Leia Organa',
        'cpf': '0e3a25d0-b2d9-11e8-96f8-529269fb1459',
        'ultimaConsulta': datetime.utcnow() - timedelta(days=20),
        'ultimaCompraCC': {
            'date': datetime.utcnow() - timedelta(days=1),
            'valor': 865998.55
        },
        'movimentacaoFinanceira': [
            {
            "tipo": "cartao-galactico",
            "valor": 865998.55,
            "data": datetime.utcnow() - timedelta(days=1)
            },
            {
            "tipo": "cartao-galactico",
            "valor": 98565.57,
            "data": datetime.utcnow() - timedelta(days=5)
            }
        ]
    },
    {
        'nome': 'Owen Lars',
        'cpf': '39729a84-b2d9-11e8-96f8-529269fb1459',
        'ultimaConsulta': datetime.utcnow(),
        'ultimaCompraCC': None,
        'movimentacaoFinanceira': [
            {
            "tipo": "transferencia",
            "valor": 86900.00,
            "data": datetime.utcnow() - timedelta(days=5)
            },
            {
            "tipo": "transferencia",
            "valor": 8996573.00,
            "data": datetime.utcnow() - timedelta(days=15)
            },
            {
            "tipo": "transferencia",
            "valor": 69853.00,
            "data": datetime.utcnow() - timedelta(days=26)
            }
        ]
    },
    {
        'nome': 'Beru Whitesun lars',
        'cpf': '5c4b34ee-b2d9-11e8-96f8-529269fb1459',
        'ultimaConsulta': datetime.utcnow() - timedelta(days=55),
        'ultimaCompraCC': {
            'date': datetime.utcnow() - timedelta(days=12),
            'valor': 52336.95
        },
        'movimentacaoFinanceira': [
            {
            "tipo": "transferencia",
            "valor": 987562.00,
            "data": datetime.utcnow() - timedelta(days=5)
            },
            {
            "tipo": "cartao-galactico",
            "valor": 52336.95,
            "data": datetime.utcnow() - timedelta(days=12)
            },
            {
            "tipo": "transferencia",
            "valor": 5689.00,
            "data": datetime.utcnow() - timedelta(days=20)
            }
        ]
    },
]

for customer in data:
    es.index(index='customer', doc_type='customer', body=customer)
