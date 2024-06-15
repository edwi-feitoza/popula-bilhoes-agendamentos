import random

class Produtos:
    def __init__(self):
        self.__produtos = []

        self.__fundos_aplicacoes = 5
        self.__ted = 12
        self.__tef = 17
        self.__pix = 23
        self.__cd = 24
        self.__boleto = 25
        self.__pix_auto = 26

        self.__produtos.append(self.__fundos_aplicacoes)
        self.__produtos.append(self.__ted)
        self.__produtos.append(self.__tef)
        self.__produtos.append(self.__pix)
        self.__produtos.append(self.__cd)
        self.__produtos.append(self.__boleto)
        self.__produtos.append(self.__pix_auto)

        self.__pesos = []

        self.__pesos.append(0.0)
        self.__pesos.append(0.04)
        self.__pesos.append(0.09)
        self.__pesos.append(0.27)
        self.__pesos.append(0.05)
        self.__pesos.append(0.55)
        self.__pesos.append(0.0)

    def get_mil_produtos(self):
        return random.choices(
            population=self.__produtos,
            weights=self.__pesos,
            k=1000
        )
