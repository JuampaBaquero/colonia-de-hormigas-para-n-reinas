import time
import numpy as np
from conf import Coord
from conf import condiciones_feromonas
from Ciclo import Ciclo
import sys

def imprimir_tablero(N: int, coordenadas: list[Coord]) -> None:
    tablero: np.ndarray = np.full((N, N), '☐')
    for pos in coordenadas:
        tablero[pos] = '♛'

    print(tablero)

def prueba_ciclo(N: int, iteraciones: int) -> None:
    ciclo: Ciclo = Ciclo(N, **condiciones_feromonas)
    tiempo, (sol_optima, conflictos, coordenadas) = ciclo.ciclar(iteraciones) #type: ignore

    print(f'Las hormigas {'SI' if sol_optima else 'NO'} alcanzaron una solución óptima\n')
    print(f'Hay {conflictos} conflictos')
    print(f'El tablero es: ')
    imprimir_tablero(N, coordenadas) # type: ignore

    print(f'La tin se demoró: {tiempo}')

def prueba_indef(N: int) -> None:
    ciclo: Ciclo = Ciclo(N, **condiciones_feromonas)
    tiempo, (iteraciones, coordenadas) = ciclo.ciclar_indef() #type: ignore

    print(f'Las hormigas alcanzaron una solución óptima en {iteraciones} pasos')
    print(f'El tablero es: ')
    imprimir_tablero(N, coordenadas) # type: ignore

    print(f'La tin se demoró: {tiempo}')
        
def main(N: int, iteraciones: int) -> None:
    prueba_indef(N)

if __name__ == "__main__":
    args: list[str] = sys.argv[1:]
    main(int(args[0]), int(args[1]))