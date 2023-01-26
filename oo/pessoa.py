class Pessoa:
    #atributo de classe
    olhos = 2

    #atributos de instancia
    def __init__(self, *filhos, nome=None, idade=None ):
        self.nome = nome
        self.idade = idade

        #atributo composto
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    luciano = Pessoa(nome='Luciano')
    renzo = Pessoa(luciano, nome='Renzo')
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
