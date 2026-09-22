import numpy as np
from conf import Coord
from Conflictos import Conflictos
from Feromonas import Feromonas

class Hormiga:

    def __init__(self, N: int, conflictos: Conflictos, feromonas: Feromonas, alpha: float, beta: float) -> None: 
        self.N: int = N
        self.alpha: float = alpha
        self.beta: float = beta
        self.reinas: list[Coord] = []
        self.conflictos: Conflictos = conflictos
        self.feromonas: Feromonas = feromonas

    def __heuristica_ind(self, val: int) -> float:
        return (
            1 / (1 + val)
        )

    def __heuristica(self, val: np.ndarray) -> np.ndarray:
        return (
            1 / (1 + val)
        )
    def __vector_de_probabilidad(self, indice: int) -> np.ndarray:

        col_escogidas: list[int] = [y for _, y in self.reinas]

        fila_conflictos: np.ndarray = self.conflictos.matriz[indice]
        fila_taus: np.ndarray = self.feromonas.matriz[indice]

        n_vector: np.ndarray = self.__heuristica(fila_conflictos)
        factores: np.ndarray = (n_vector ** self.alpha) * (fila_taus ** self.beta)
        if col_escogidas:
            factores[col_escogidas] = 0.0
        #Normalizando... 
        probabilidades: np.ndarray = factores / np.sum(factores)

        return probabilidades
        

    def __elegir_posicion_prob(self, indice: int) -> Coord:

        vector: np.ndarray = self.__vector_de_probabilidad(indice)
        col: int = np.random.choice(np.arange(self.N), p = vector)
        col = np.random.choice(np.arange(self.N), p = vector)
        return(indice, col)

    def __conflictos_globales(self) -> int:

        conflictos_globales: int = 0
        for pos1 in self.reinas:
            for pos2 in self.reinas:

                if pos1 == pos2:
                    continue 

                difx: bool = (pos1[0] == pos2[0])
                dify: bool = (pos1[1] == pos2[1])
                diag_principal: bool = (pos1[0] - pos1[1] == pos2[0] - pos2[1])
                diag_secundaria: bool = (pos1[0] + pos1[1] == pos2[0] + pos2[1])
                if difx or dify or diag_principal or diag_secundaria:
                    conflictos_globales += 1

        return int(conflictos_globales / 2)

    def poner_reinas(self) -> int:
        for i in range(self.N):
            pos: Coord = self.__elegir_posicion_prob(i)
            self.conflictos.reinear(pos)
            self.reinas.append(pos)

        return self.__conflictos_globales()

    def actualizar_feromonas(self, conflictos_globales: int) -> None:
        self.feromonas.evaporar_feromonas()
        self.feromonas.actualizar_escogidas(
            self.reinas,
            self.__heuristica_ind(conflictos_globales)
        )

    def resetiar(self) -> None:
        self.conflictos.reiniciar()
        self.reinas = []
