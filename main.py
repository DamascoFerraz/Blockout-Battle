#arquivo principal que vai rodar o jogo
from importar import *

os.system("cls")

run = True

while(run):
    players = [
        {
            "tabuleiro" : tabuleiroVazio(),
            "vetor_dmg" : vetorVazio()
        },
        {
            "tabuleiro" : tabuleiroVazio(),
            "vetor_dmg" : vetorVazio()
        }
    ]

    printTabuleiro(players[1])
    input("rodou...")
    break