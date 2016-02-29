#jogando.py

from batalha_naval import BatalhaNaval

t = BatalhaNaval()

t.cria_tabuleiro(5,5)

t.distribuir_navios()

t.jogada(0,1)