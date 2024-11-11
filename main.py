#arquivo principal que vai rodar o jogo
from importar import *

os.system("cls")

run = True

while(run):
    players = [
        {
            "tabuleiro" : tabuleiroVazio(),
            "vetor_dmg" : vetorVazio(),
            "vida" : 10,
            "mao" : gerarPecas()
        },
        {
            "tabuleiro" : tabuleiroVazio(),
            "vetor_dmg" : vetorVazio(),
            "vida" : 10,
            "mao" : gerarPecas()
        }
    ]
    turno = 0
    game = True
    while(game):

        os.system("cls")

        if turno % 2 == 0:
            ativo = 0
            inativo = 1
        else:
            ativo = 1
            inativo =0

        atualizarVetor(players[ativo],players[inativo])

        printRodada(turno,players)

        players[ativo]['mao'] = gerarPecas()

        printMao(players[ativo]['mao'])

        while True:
            try:
                escolha = int(input(">"))
                if (escolha-1<len(players[ativo]['mao']) and escolha-1>0) or (escolha!=int):
                    break
                else:
                    print("input inválido")
            except:
                print("input inválido")

        while True:
            posicao = input("digite a posicao onde colocará a peça (pelo primeiro bloco a esquerda)\n>")
            try:
                x = int(posicao[1])-1
                y = str(posicao[0].upper())
            except:
                print("input inválido")

            validy = ''.join(chr(i) for i in range(ord('A'), ord('A') + 5))
            if y in validy:
                if(pecaColocavel(string.ascii_uppercase.index(y),x,players[ativo]['mao'][escolha-1],players[ativo]['tabuleiro'])):
                    colocarPeca(string.ascii_uppercase.index(y),x,players[ativo]['mao'][escolha-1],players[ativo]['tabuleiro'])
                    break
                else:
                    print("input inválido")

        atualizarVetor(players[ativo],players[inativo])

        players[ativo]['vida']-= atualizarVida(players[ativo]['vetor_dmg'])

        if players[ativo]['vida']<=0:
            printRodada(turno,players)
            print("╠══════════════════════════╣")
            print(f"├═════Jogador {inativo+1} venceu══════┤")
            print("╠══════════════════════════╣")
            break
        turno+=1
    run = False