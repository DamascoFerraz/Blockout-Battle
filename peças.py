if __name__ == "__main__":
   print("tá perdido filhão?")
else:
    import os
    try:
        import numpy as np
    except ModuleNotFoundError:
        os.system("cls")
        print("Para Jogar, instale o pacote Numpy com o comando [pip install numpy] no seu CMD")
        input("aperte ENTER para sair da aplicação...")
        exit()
    # ------------------------ CLASSES ----------------------------
    class Peca(np.ndarray):
        def __new__(cls, input_array):
            obj = np.asarray(input_array).view(cls)
            return obj

        def __array_finalize__(self, obj):
            if obj is None: return
            self.info = "Esta é uma peça do jogo"

    # ------------------------ DEFININDO PEÇAS ----------------------------
    pecas = []
    
    pecas.append(Peca([
            ["D", 0],
            ["D", 0],
            ["D","A"]
        ]))