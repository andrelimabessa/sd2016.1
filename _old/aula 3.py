from batalhanaval import Batalha_Naval

tabuleiro = Batalha_Naval(5)

tabuleiro.mostraTabuleiro()

tabuleiro.alocarFrota([[0, 3], [2, 4], [4, 2]])

tabuleiro.mostraTabuleiro()

tabuleiro.atirar([0, 2])
tabuleiro.atirar([0, 3])