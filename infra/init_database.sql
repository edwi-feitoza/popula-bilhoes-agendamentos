CREATE DATABASE IF NOT EXISTS agendamentopagamentos;
GO
USE agendamentopagamentos;
GO
CREATE TABLE IF NOT EXISTS agendamento_pagamento (
    id CHAR(36) NOT NULL,
    id_conta CHAR(36) NOT NULL,
    data_efetivacao DATETIME NOT NULL,
    id_produto DECIMAL(6,0) NOT NULL,
    data_criacao DATETIME NOT NULL,
    data_atualizacao DATETIME NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    valor DECIMAL(17,2) NOT NULL,
    numero_particao TINYINT NOT NULL,
    PRIMARY KEY(id, data_efetivacao, numero_particao)
)
PARTITION BY RANGE COLUMNS(data_efetivacao)
SUBPARTITION BY HASH (numero_particao)
SUBPARTITIONS 16 (
    PARTITION p20240608 VALUES LESS THAN ('2024-06-09') ENGINE = InnoDB,
    PARTITION p20240609 VALUES LESS THAN ('2024-06-10') ENGINE = InnoDB
);
