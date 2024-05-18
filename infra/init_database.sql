CREATE DATABASE IF NOT EXISTS teste_bilhoes;
GO
USE teste_bilhoes;
GO
CREATE TABLE IF NOT EXISTS agendamento_bilhao(
    id CHAR(36) NOT NULL,
    id_conta CHAR(36) NOT NULL,
    data_efetivacao DATETIME NOT NULL,
    tipo_produto enum('TED', 'TEF', 'PIX'),
    data_criacao DATETIME NOT NULL,
    data_atualizacao DATETIME NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    PRIMARY KEY(id, data_efetivacao, tipo_produto)
);