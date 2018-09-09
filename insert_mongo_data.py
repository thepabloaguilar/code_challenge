from pymongo import MongoClient

# Make Mongo Connection
client = MongoClient('mongodb://super_user:super_password@localhost:27018/challenge_db?authSource=challenge_db')
collection = client['challenge_db']['customer']

data = [
    {
        'nome': 'Luke Skywalker',
        'endereco': 'Tatooine',
        'cpf': 'f7bc221a-3dca-43b3-bc71-2704e9815fd4',
        'fonteDeRenda': 'Ordem Jedi',
        'bens': [
            {
            'tipo': 'Starships',
            'descricao': 'Executor-class star dreadnought',
            'avaliadoEm': 1143350000.00,
            'quitado': True
            },
            {
            'tipo': 'Starships',
            'descricao': 'Sentinel-class landing craft',
            'avaliadoEm': 240000.00,
            'quitado': True
            }
        ]
    },
    {
        'nome': 'Leia Organa',
        'endereco': 'Alderaan',
        'cpf': '0e3a25d0-b2d9-11e8-96f8-529269fb1459',
        'fonteDeRenda': 'Império Galáctico',
        'bens': [
            {
            'tipo': 'Starships',
            'descricao': 'DS-1 Orbital Battle Station',
            'avaliadoEm': 1000000000000.00,
            'quitado': False
            },
            {
            'tipo': 'Starships',
            'descricao': 'YT-1300 light freighter',
            'avaliadoEm': 100000.00,
            'quitado': True
            },
            {
            'tipo': 'Starships',
            'descricao': 'BTL Y-wing',
            'avaliadoEm': 134999.00,
            'quitado': True
            }
        ]
    },
    {
        'nome': 'Owen Lars',
        'endereco': 'Tatooine',
        'cpf': '39729a84-b2d9-11e8-96f8-529269fb1459',
        'fonteDeRenda': 'Família Lars',
        'bens': [
            {
            'tipo': 'Starships',
            'descricao': 'T-65 X-wing',
            'avaliadoEm': 149999.00,
            'quitado': False
            },
            {
            'tipo': 'Starships',
            'descricao': 'Lambda-class T-4a shuttle',
            'avaliadoEm': 240000.00,
            'quitado': False
            }
        ]
    },
    {
        'nome': 'Beru Whitesun lars',
        'endereco': 'Tatooine',
        'cpf': '5c4b34ee-b2d9-11e8-96f8-529269fb1459',
        'fonteDeRenda': 'Família Lars',
        'bens': None
    },
]

collection.insert_many(data)
