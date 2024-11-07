if __name__ == "__main__":
   print("tá perdido filhão?")
else:
   
   def tabuleiroVazio():
    return [[0 for _ in range(5)] for _ in range(5)]
   def vetorVazio():
     return[0 for _ in range(5)]
   
   def printTabuleiro(tabuleiro = list):
    a = {
        1 : "A",
        2 : "B",
        3 : "C",
        4 : "D",
        5 : "E",
        6 : "F",
        7 : "G",
        8 : "H",
        9 : "I",
        10 : "J"
    }
    for i in range(1,len(tabuleiro)):
        print(f"{a[i]} {tabuleiro[i-1]}")