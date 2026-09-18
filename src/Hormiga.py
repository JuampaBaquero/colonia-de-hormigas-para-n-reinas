import numpy as np
from conf import Coord
from Conflictos import Conflictos
from Feromonas import Feromonas

class Hormiga:

    def __init__(self, N: int, conflictos: Conflictos, feromonas: Feromonas) -> None: 
        self.N: int = N
        reinas: list[Coord] = []
        self.conflictos: Conflictos = conflictos
        self.feromonas: Feromonas = feromonas

    def heuristica(self, val: int) -> float:
        return (
            1 / (1 + float(val))
        )

    def calcular_mayor_prob(self, indice: int) -> Coord:
        max: int = 0
        max_factor: float = 0.0
        for i in range(self.N):
            conf: int = self.conflictos.matriz[indice][i]
            n = self.heuristica(conf)

            tau: float = self.feromonas.matriz[indice][i]

            factor: float = n * tau

            if factor > max_factor:
                max = i
                max_factor = factor

        return (indice, max)

    def poner_reinas(self) -> None:
        for i in range(self.N):
            self.conflictos.reinear(self.calcular_mayor_prob(i))