import numpy as np
from conf import Coord

class Feromonas:

    def __init__(self, N: int, rho: float, tau_0: float = 1.0) -> None:
        self.N = N
        self.matriz: np.ndarray = np.full((N, N), tau_0)
        self.rho = rho
        self.tau_0 = tau_0

    def evaporar_feromonas(self) -> None:
        self.matriz = self.matriz * self.rho #fockin python

    def actualizar_escogidas(self, lista: list[Coord], factor: float) -> None:
        for coord in lista:
            self.matriz[coord] += factor

    def reset(self) -> None:
        self.matriz = np.full((self.N,self.N), self.tau_0)