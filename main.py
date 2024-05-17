from database.agendamentos_db_connection import AgendamentosDbConnection
from repository.repository import Repository
import sys
import uuid
import random
from datetime import datetime
import pytz

def create_agendamentos_to_insert(db_connection, repository):
    data_efetivacao = sys.argv[1]
    tipo_produtos = ['TED', 'TEF', 'PIX']
    timezone = pytz.timezone('America/Sao_Paulo')
    count = 0
    while count <= 65_000_000:
        list_agendamentos = []
        for i in range(1, 101):
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
        count += 100

if __name__ == '__main__':
    db_connection = AgendamentosDbConnection()
    repository = Repository()
    create_agendamentos_to_insert(db_connection.get_connection(), repository)
    db_connection.close_connection()
