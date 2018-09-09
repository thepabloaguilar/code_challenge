import os

import elasticsearch


# Devolve uma instancia de conexão com o ElasticSearch
def get_elasticsearch_connection():
    es = elasticsearch.Elasticsearch([
        {
            'host': os.getenv('ELASTICSEARCH_HOST'),
            'port': os.getenv('ELASTICSEARCH_PORT')
        }])
    return es
