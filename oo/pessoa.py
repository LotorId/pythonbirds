class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None ):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    luciano = Pessoa(nome='Luciano')
    renzo = Pessoa(luciano, nome='Renzo')
    print(luciano.nome)
    print(renzo.filhos)