from Feromonas import Feromonas
from Conflictos import Conflictos
from Hormiga import Hormiga
from conf import condiciones_feromonas
from Ciclo import Ciclo
import sys

def main(N: int, iteraciones: int) -> None:
    ciclo: Ciclo = Ciclo(N, **condiciones_feromonas)
    

if __name__ == "__main__":
    args: list[str] = sys.argv[1:]
    main(int(args[1]), int(args[2]))