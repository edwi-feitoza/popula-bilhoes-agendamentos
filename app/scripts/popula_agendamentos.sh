#!/bin/bash
export DB_DATABASE="teste_bilhoes"
export DB_HOST="mainserver.edwifeitoza.com.br"
export DB_PASSWORD="meuovocaraio"
export DB_USER="root"
for dias_para_somar in {0..364}
do
    export DATA_EFETIVACAO=`date --date "+$dias_para_somar days" +'%Y-%m-%d 00:00:00'`
    python3 ../main.py $DATA_EFETIVACAO > ~/bilhao.log 2>&1 &
done
