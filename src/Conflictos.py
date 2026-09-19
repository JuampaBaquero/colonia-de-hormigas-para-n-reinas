import numpy as np
from conf import Coord

class Conflictos:
    """
        Un ejemplo de matríz de conflictos:
        
        -1  1  1  1
         1  1 -1  1 -> Si la hormiga pone una reina acá, solo nos interesa modificar 
         1  1  1  1    las casillas afectadas hacia abajo, porque son las de las 
         2  0  1  1    hormigas que no han colocado reinas

         -> POR IMPLEMENTAR
         
    """

    def __init__(self, N: int) -> None:
        self.N = N
        self.matriz: np.ndarray = np.zeros((N, N))

    def reinear(self, pos: Coord) -> None:
        self.matriz[pos[0]][pos[1]] = -1 #-1 es reina
        self.conflictear(pos)

    def reiniciar(self) -> None:
        self.matriz[:, :] = 0

    def conflictear(self, pos: Coord) -> None:

        #arange retorna un rango pero es un arreglo de numpy :b
        i: np.ndarray = np.arange(self.N)[:, None]  # Columna
        j: np.ndarray = np.arange(self.N)[None, :]  # Fila

        mascara_columnas: np.ndarray        = (i == pos[0])
        mascara_filas: np.ndarray           = (j == pos[1])
        mascara_diagonal_princ: np.ndarray  = (i - j) == (pos[0] - pos[1])
        mascara_diagonal_secun: np.ndarray  = (i + j) == (pos[0] + pos[1])
        mascara_otras_reinas: np.ndarray    = (self.matriz != -1)

        mascara: np.ndarray = (mascara_columnas | mascara_filas | 
                               mascara_diagonal_princ | mascara_diagonal_secun) & mascara_otras_reinas

        #aplicamos...
        self.matriz[mascara] += 1 