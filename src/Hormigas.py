import numpy as np
from conf import Coord
from Conflictos import Conflictos
from tins import Feromonas

class Hormigas:

    def __init__(self, N: int, conflictos: Conflictos, feromonas: Feromonas) -> None: 
        self.N: int = N
        reinas: np.ndarray = np.full((N, N), (0, 0))
        self.conflictos: Conflictos = conflictos
        self.feromonas: Feromonas = feromonas

    def __heuristica(self, val: int) -> float:
        return (
            1 / (1 + float(val))
        )

    def __calcular_mayor_prob(self, indice: int) -> int:
        max: int = 0
        for i in range(self.N):
            conf: int = self.conflictos.matriz[indice][i]
            n = self.__heuristica(conf)

            tau: float = self.feromonas.matriz[indice][i]

            factor: float = n * tau

            if factor > max:
                max = i

        return max

    def poner_reinas() -> None:
        pass