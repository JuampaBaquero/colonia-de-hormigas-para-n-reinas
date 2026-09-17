from tins import Feromonas
from conf import valores_iniciales
import sys

def main(N: int) -> None:
    feromonas: Feromonas = Feromonas(N, **valores_iniciales)

if __name__ == "__main__":
    args: list[str] = sys.argv[1:]
    main(int(args[1]))