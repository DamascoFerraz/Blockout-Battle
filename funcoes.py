from peças import *
import random
if __name__ == "__main__":
   print("tá perdido filhão?")
else:
# region SETUP FUNCOES

  def tabuleiroVazio():
    return [[0 for _ in range(5)] for _ in range(5)]
  
  def layerVazio():
    return [["N" for _ in range(5)] for _ in range(5)]
  
  def vetorVazio():
    return[0 for _ in range(5)]
  
  def gerarPecas():
    mao = []
    for _ in range(0,5):
      mao.append(pecas[random.randint(0,len(pecas)-1)])
    return mao
  
#endregion

# region interface funcoes

  def printTabuleiro(tabuleiro = list):
    a = {
        0 : "A",
        1 : "B",
        2 : "C",
        3 : "D",
        4 : "E",
        5 : "F",
        6 : "G",
        7 : "H",
        8 : "I",
        9 : "J"
    }
    for i in range(len(tabuleiro)):
        print(f"{a[i]} ", end=' ')
        for ii in range(len(tabuleiro[i])):
          print(f" {tabuleiro[i][ii]} ".replace("0"," "), end='')
          if ii+1==len(tabuleiro[i]):
            print("", end='\n')
          else:
            print("|", end='')

  def printColocandoPeca(tabuleiro = list,layer = list):
    a = {
        0 : "A",
        1 : "B",
        2 : "C",
        3 : "D",
        4 : "E",
        5 : "F",
        6 : "G",
        7 : "H",
        8 : "I",
        9 : "J"
    }
    for i in range(len(tabuleiro)):
        print(f"{a[i]} ", end=' ')
        for ii in range(len(tabuleiro[i])):
          if layer[i][ii]!='N':
            print(f"[{layer[i][ii]}]".replace("0"," "), end='')
          else:
            print(f" {tabuleiro[i][ii]} ".replace("0"," "), end='')
          if ii+1==len(tabuleiro[i]):
            print("", end='\n')
          else:
            print("|", end='')

  def overflowX(x,p,t):
    if x+len(p[0])-len(t[0])<0:
      return 0
    return x+len(p[0])-len(t[0])

  def overflowY(y,p,t):
    if y+len(p)-len(t)<0:
      return 0
    return y+len(p)-len(t)

  def printVetor(vetor = list):
    print(f"  {vetor}".replace(", "," | ").replace('[','! ').replace(']',' !'))

  def printVida(vida):
    print(f'     HP[{vida}]', end='')
    for _ in range(vida):
      print('█', end='')
    for _ in range(10-vida):
      print('░', end='')
    print("")
  
  def printRodada(turn, players):
    if turn % 2 == 0:
      first = 0
      last = 1
    else:
      first = 1
      last = 0

    print(f'════════╣TURNO {turn}╠════════')
    printVida(players[last]['vida'])
    printVetor(players[last]['vetor_dmg'])

    printTabuleiro(players[last]['tabuleiro'])

    print("├───────────────────────┤")
    printTabuleiro(players[first]['tabuleiro'])

    printVetor(players[first]['vetor_dmg'])
    printVida(players[first]['vida'])
    print(f'═══╣ VEZ D JOGADOR {first+1} ╠═══')

  def printRodadaColocandoPeca(turn, players,layer):
    if turn % 2 == 0:
      first = 0
      last = 1
    else:
      first = 1
      last = 0

    print(f'════════╣TURNO {turn}╠════════')
    printVida(players[last]['vida'])
    printVetor(players[last]['vetor_dmg'])

    printTabuleiro(players[last]['tabuleiro'])

    print("├───────────────────────┤")
    printColocandoPeca(players[first]['tabuleiro'],layer)

    printVetor(players[first]['vetor_dmg'])
    printVida(players[first]['vida'])
    print(f'═══╣ VEZ D JOGADOR {first+1} ╠═══')

  def printMao(mao):
    print("Escolha uma peça para posicionar:")
    for i in range(len(mao)):

      print(f"[{i+1}]:")

      for ii in range(len(mao[i])):
        print("   ", end='')
        for iii in range(len(mao[i][ii])):
          if mao[i][ii][iii] == "N":
            print("   ",end='')
          else:
            print(f"[{mao[i][ii][iii]}]", end='')

          if iii==len(mao[i][ii]):
            print("", end='\n')

        print("", end='\n')
      print("", end='\n')

#endregion

# region acoes funcoes

  def pecaColocavel(y,x,p,t):
    if x+len(p[0])>len(t[0]):
      return False
    elif y+len(p)>len(t):
      return False
    elif x<0 or y<0:
      return False
    else:
      return True
    
  def colocarPeca(y,x,p,t):
    for i in range(len(p)):
      for ii in range(len(p[i])):
        if p[i][ii]!='N':
          t[y+i][x+ii] = p[i][ii]

# endregion

# region turno funcoes

  def atualizarVida(d):
    dmgtotal = np.sum(d)
    if dmgtotal>0:
      return dmgtotal
    else:
      return 0
    
  def atualizarVetor(ativo,inativo):
      
      for i in range(len(ativo['vetor_dmg'])):
        
        ativo['vetor_dmg'][i] = 0

        for ii in range(len(ativo['vetor_dmg'])):

          if inativo['tabuleiro'][ii][i] == "A":
                ativo['vetor_dmg'][i]+=1
                
          if ativo['tabuleiro'][ii][i] == "D":
                ativo['vetor_dmg'][i]-=1
        if ativo['vetor_dmg'][i] < 0:
          ativo['vetor_dmg'][i] = 0

# endregion