from conf import Coord, macro_condiciones
from Feromonas import Feromonas
from Conflictos import Conflictos
from Hormiga import Hormiga
from Mediciones import Mediciones

class Ciclo:

    def __init__(self, N: int, tau_min: float, rho: float, alpha: float, beta: float) -> None:
        self.N = N
        self.tau_min = tau_min
        self.rho = rho
        self.conflictos: Conflictos = Conflictos(N)
        self.feromonas: Feromonas = Feromonas(N, rho, tau_min)
        self.hormiga: Hormiga = Hormiga(N, self.conflictos, self.feromonas, alpha, beta)

    @Mediciones.medir_tiempo
    def ciclar(self, num_ciclos: int) -> tuple[bool, int, list[Coord]]:

        sol: list[Coord] = []
        mejor_caso: int = int(self.N * (self.N + 1) / 2)
        #sum_{i = 0}^N{N} = N(N+1) / 2 (gracias Gauss)
        
        for _ in range(num_ciclos * self.N):
            conf_globales = self.hormiga.poner_reinas()

            if conf_globales == 0:
                sol = self.hormiga.reinas.copy()
                return (True, 0, sol)

            if conf_globales < mejor_caso:
                mejor_caso = conf_globales
                sol = self.hormiga.reinas.copy()

            self.hormiga.actualizar_feromonas(conf_globales)
            self.hormiga.resetiar()

        return (False, mejor_caso, sol)

    @Mediciones.medir_tiempo
    def ciclar_indef(self) -> tuple[int, list[Coord]]:

        sol: list[Coord] = []
        i: int = 1
        j: int = 1
        mejor_caso: int = int(self.N * (self.N + 1) / 2)
        while True:
            self.feromonas.reset()
            i = 1
            while i <= macro_condiciones['micro_iteraciones']:
                conf_globales = self.hormiga.poner_reinas()

                if conf_globales == 0:
                    sol = self.hormiga.reinas.copy()
                    return (j, sol)
                
                if conf_globales < mejor_caso:
                    mejor_caso = conf_globales
                    sol = self.hormiga.reinas.copy()

                self.hormiga.actualizar_feromonas(conf_globales)
                self.hormiga.resetiar()
                i += 1

            j += 1