class Repository:
    def insert_agendamentos(self, connection, rows):
        try:
            insert_query = '''INSERT INTO agendamento_bilhao (id, id_conta, data_efetivacao,
             tipo_produto, data_criacao, data_atualizacao, descricao)
              VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            cursor = connection.cursor()
            cursor.executemany(insert_query, rows)
            connection.commit()
            cursor.close()
        except Exception as error:
            print('Failed to insert agendamentos in table due to error {}.'.format(error))
