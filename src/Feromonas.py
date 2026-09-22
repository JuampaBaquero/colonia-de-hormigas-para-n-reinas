import numpy as np
from conf import Coord

class Feromonas:

    def __init__(self, N: int, rho: float, tau_min: float = 1.0) -> None:
        self.N = N
        self.matriz: np.ndarray = np.full((N, N), 1) #Llenamos la matríz con 1's 
        self.rho = rho
        self.tau_min = tau_min

    def evaporar_feromonas(self) -> None:
        self.matriz = self.matriz * self.rho #fockin python
        menores_a_tau_min: np.ndarray = self.matriz < self.tau_min
        self.matriz[menores_a_tau_min] = self.tau_min

    def actualizar_escogidas(self, lista: list[Coord], factor: float) -> None:
        for coord in lista:
            self.matriz[coord] += factor

    def reset(self) -> None:
        self.matriz = np.full((self.N,self.N), self.tau_min)