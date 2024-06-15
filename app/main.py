from database.agendamentos_db_connection import AgendamentosDbConnection
from repository.repository import Repository
from service.produtos import Produtos
from service.utilities import Utilities
import sys
import uuid
import random
from datetime import datetime
import pytz

def create_agendamentos_to_insert(db_connection, repository, produtos, utilities):
    data_efetivacao = sys.argv[1]
    timezone = pytz.timezone('America/Sao_Paulo')
    produtos = produtos.get_mil_produtos()
    count = 0
    while count <= 65_000_000:
        list_agendamentos = []
        for i in range(0, 999):
            id_agendamento = str(uuid.uuid4())
            id_conta = str(uuid.uuid4())
            tipo_produto = random.choice(tipo_produtos)
            data_criacao = datetime.now(timezone).isoformat()
            data_atualizacao = datetime.now(timezone).isoformat()
            descricao = 'bla bla bla bla bla bla bla bla bla bla bla bla bla bla bl'
            list_agendamentos.append((id_agendamento, id_conta, data_efetivacao,
                                      tipo_produto, data_criacao,
                                      data_atualizacao, descricao))
        repository.insert_agendamentos(db_connection, list_agendamentos)
        count += 1000

if __name__ == '__main__':
    db_connection = AgendamentosDbConnection()
    repository = Repository()
    produtos = Produtos()
    utilities = Utilities()
    create_agendamentos_to_insert(db_connection.get_connection(),
                                  repository,
                                  produtos,
                                  utilities)
    db_connection.close_connection()
