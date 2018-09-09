import os

from sqlalchemy import create_engine, pool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

postgres_uri = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
    os.getenv('POSTGRES_USER'),
    os.getenv('POSTGRES_PASSWORD'),
    os.getenv('POSTGRES_HOST'),
    os.getenv('POSTGRES_PORT'),
    os.getenv('POSTGRES_DB')
)

# Instancia a Engine de conexão com o Postgres
postgres_db = create_engine(
    postgres_uri,
    poolclass=pool.NullPool,
    echo=True
)

# Objeto para criar sessões no BD
PostgresSession = scoped_session(sessionmaker(bind=postgres_db))

# Objeto para mapear as classes com as tabelas do BD
PostgresBase = declarative_base()
PostgresBase.metadata.bind = postgres_db
PostgresBase.query = PostgresSession.query_property()