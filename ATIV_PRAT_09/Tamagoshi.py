# 4) Crie uma classe que modele um Tamagochi (Bichinho Eletrônico):
# a) Atributos
# i) Nome
# ii) Fome
# iii) Saúde
# iv) Idade.
# b) Métodos
# i) alterar_nome,
# ii) alterar_fome
# iii) alterar_saude
# iv) alterar_idade
# v) retornar_nome
# vi) retornar_nome
# vii) retornar_saude
# viii) retornar_idade


class Tamagoshi:
    def __init__(self):
        self.name = None
        self.fome = None
        self.saude = None
        self.idade = None

    def set_name(self, name):
        self.name = name

    def set_fome(self, fome):
        self.fome = fome

    def set_saude(self, saude):
        self.saude = saude

    def set_idade(self, idade):
        self.idade = idade

    def get_name(self):
        return self.name

    def get_fome(self):
        return self.fome

    def get_saude(self):
        return self.saude

    def get_idade(self):
        return self.idade
