import numpy as np

class Feromonas:

    def __init__(self, N: int, rho: float, tau_0: float = 1.0) -> None:
        self.matriz: np.ndarray = np.full((N, N), tau_0)
        self.rho = rho

    def evaporar_feromonas(self) -> None:
        self.matriz = self.matriz * self.rho #fockin python

    