class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(p.cumprimentar())
    print(id(p))
    print(p.nome)