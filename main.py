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

        layer = layerVazio()

        atualizarVetor(players[ativo],players[inativo],layer)

        printRodada(turno,players)

        players[ativo]['mao'] = gerarPecas()

        printMao(players[ativo]['mao'])

        while True:
            try:
                escolha = int(input(">"))
                if (escolha-1<len(players[ativo]['mao']) and escolha-1>=0):
                    pecaEscolhida = players[ativo]['mao'][escolha-1]
                    break
                else:
                    print("input inválido")
            except:
                print("input inválido")

        x=0
        y=0

        while True:
            os.system("cls")

            layer = layerVazio()

            colocarPeca(y,x,pecaEscolhida,layer)

            atualizarVetor(players[ativo],players[inativo],layer)

            printRodadaColocandoPeca(turno,players,layer)

            while True:
                try:
                    resposta = str(input("Mova a peça (W,A,S,D) e posicione-a (1),\nvoce pode rotaciona-la com (R)\n>"))
                    break
                except:
                    pass

            if resposta == "A" or resposta == "a":
                if pecaColocavel(y,x-1,pecaEscolhida,layer):
                    x-=1
                else:
                    pass
            elif resposta == "D" or resposta == "d":
                if pecaColocavel(y,x+1,pecaEscolhida,layer):
                    x+=1
                else:
                    pass
            elif resposta == "S" or resposta == "s":
                if pecaColocavel(y+1,x,pecaEscolhida,layer):
                    y+=1
                else:
                    pass
            elif resposta == "W" or resposta == "w":
                if pecaColocavel(y-1,x,pecaEscolhida,layer):
                    y-=1
                else:
                    pass
            elif resposta == "R" or resposta == "r":

                pecaEscolhida = np.rot90(pecaEscolhida)
                
                if not pecaColocavel(y,x,pecaEscolhida,layer):
                    x-=overflowX(x,pecaEscolhida,layer)
                    y-=overflowY(y,pecaEscolhida,layer)
                    
            elif resposta == "1":
                colocarPeca(y,x,pecaEscolhida,players[ativo]['tabuleiro'])
                break
            else:
                pass
                    
        atualizarVetor(players[ativo],players[inativo],layer)
        layer = layerVazio()
        players[ativo]['vida']-= atualizarVida(players[ativo]['vetor_dmg'])

        if players[ativo]['vida']<=0:
            printRodada(turno,players)
            print("╠══════════════════════════╣")
            print(f"├═════Jogador {inativo+1} venceu══════┤")
            print("╠══════════════════════════╣")
            break
        turno+=1
    
    run = False