import random

class Utilities:
    def get_valor_agendamento(self):
        return round(random.uniform(1.01, 5000.99), 2)

    def get_numero_particao(self, id_conta):
        last_hex_char = id_conta[-1]
        decimal_value = int(last_hex_char, 16)
        return decimal_value + 1
