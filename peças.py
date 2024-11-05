import numpy as np

class Peca(np.ndarray):
    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return
        self.info = "Esta é uma peça do jogo"

    

peca1 = Peca([
        [0, 0, 0],
        [0, 0, 0]
    ])

print(peca1)