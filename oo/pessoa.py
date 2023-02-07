class Pessoa:
    # atributo de classe
    olhos = 2

    # atributos de instancia
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

        # atributo complexo
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe} Aperto de mao'
    pass

class Mutante(Pessoa):
    olhos = 3
    pass

if __name__ == '__main__':
    luciano = Homem(nome='Luciano')
    renzo = Mutante(luciano, nome='Renzo')
    print(luciano.nome)
    print(renzo.filhos)
    for filho in renzo.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Loures'
    del renzo.filhos
    print(luciano.sobrenome)
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(Pessoa.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe())
    carlos = Homem(nome='Carlos')
    print(carlos.nome)
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(renzo.olhos)
    print(luciano.cumprimentar())
    print(renzo.cumprimentar())
