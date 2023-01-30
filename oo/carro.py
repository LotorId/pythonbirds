"""
Voce deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1 - motor
2 - direcao

O motor terá a responsabilidade de controlar a velocidade
ele oferece os seguintes atributos
1 - atributo de velocidade
2 - metodo acelerar, que devera incrementar a velocidade de uma unidade
3 - metodo frear que devera decrementar a velocidade em duas unidades

A direcao tera a responsabilidade de controlar a direcao. ela oferece os
seguintes valores
1 - valor de direcao com valores possiveis: norte sul leste oeste
2 - girar a direita
3 - dirar a esquerda

  N
O   L
  S

exemplo

>>> motor = Motor()

motor.velocidade
0
motor.acelerar()
motor.velocidade

1
motor.acelerar()
motor.velocidade
2
motor.acelerar()
motor.velocidade
3

motor.frear()
motor.velocidade
2
motor.frear()
motor.velocidade
1

direcao = Direcao()
direcao.valor
norte

direcao.girar_a_direita()
direcao.valor()
leste

direcao.girar_a_direita()
direcao.valor()
sul


carro = Carro(direcao, motor)
carro.calcular_velocidade()
1

carro.acelerar()
carro.frear()

carro.girar_a_direita()
carro.girar_a_esquerda()
"""

NORTE='Norte'
SUL='Sul'
LESTE='Leste'
OESTE='Oeste'

class Direcao:
    rotacao_a_direita = { NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE }
    rotacao_a_esquerda = { NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda[self.valor]

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade=max(0, self.velocidade)


