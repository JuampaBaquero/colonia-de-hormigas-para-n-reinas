import numpy as np
from conf import Coord

class Conflictos:
    """
        Un ejemplo de matríz de conflictos:
        
        -1  1  1  1
         1  1 -1  1 -> Si la hormiga pone una reina acá, solo nos interesa modificar 
         1  1  1  1    las casillas afectadas hacia abajo, porque son las de las 
         2  0  1  1    hormigas que no han colocado reinas
         
    """

    def __init__(self, N: int) -> None:
        self.matriz: np.ndarray = np.zeros((N, N))

    def reinear(self, pos: Coord) -> None:
        self.matriz[pos[0]][pos[1]] = -1 #-1 es reina
        self.conflictear(pos)


    def conflictear(self, pos: Coord) -> None:

        #solo la fila de la reina
        for i in range(pos[0], len(self.matriz)):
            if self.matriz[i][pos[1]] != -1:
                self.matriz[i][pos[1]] += 1

        for i in range(pos[1], len(self.matriz)):
            if self.matriz[pos[0]][i] != -1:
                self.matriz[pos[0]][i] += 1

        coso: int = 1
        for i in range(len(self.matriz[pos[0]])):
            if i > pos[0]:
                self.matriz[pos[0] - coso][i] += 1
                self.matriz[pos[0] + coso][i] += 1
                coso += 1