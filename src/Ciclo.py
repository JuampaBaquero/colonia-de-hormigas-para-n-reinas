import time
from functools import wraps #Para medir el tiempo 
from Feromonas import Feromonas
from Conflictos import Conflictos
from Hormiga import Hormiga

class Ciclo:

    def __init__(self, N: int, tau_0: float, rho: float) -> None:
        self.N = N
        self.tau_0 = tau_0
        self.rho = rho
        self.conflictos: Conflictos = Conflictos(N)
        self.feromonas: Feromonas = Feromonas(N, rho, tau_0)
        self.hormiga: Hormiga = Hormiga(N, self.conflictos, self.feromonas)

    def ciclar(self, num_ciclos: int) -> None:

        for _ in range(num_ciclos * self.N):    
            conf_globales: int = self.hormiga.poner_reinas()
            self.hormiga.actualizar_feromonas(conf_globales)
            self.conflictos.reiniciar()
