from Pruebas import Pruebas as p
from conf import condiciones_feromonas, macro_condiciones
import sys

def verificar_input(N: str, iteraciones: str, probar_varias: str = 'n') -> tuple[int, int, bool]:
    while True:
        try:
            n: int = int(N)
            if n < 4:
                print('No puedes tener un N < 4...')
                N = input('Ingresa otro valor de N: ')
            else:
                break
        except ValueError:
            print('N tiene que ser un número...')
            N = input('Ingresa el valor de N: ')

    while True:
        try:
            iters: int = int(iteraciones)
            if iters < 0:
                print('Las iteraciones deben ser mayores o iguales a 0...')
                iteraciones = input('Ingresa otro valor de iteraciones: ')
            else:
                break
        except ValueError:
            print('Iteraciones tiene que ser un número...')
            iteraciones = input('Ingresa el valor de iteraciones: ')

    probar: bool = (probar_varias == 's')

    return n, iters, probar

def main(N: int, iteraciones: int, probar_muchas: bool = False) -> None:

    print(f'Corriendo algoritmo con estas condiciones:\n{condiciones_feromonas = }\n{macro_condiciones = }')

    if probar_muchas:
        if iteraciones == 0:
            p.probar_n_tableros(N, iteraciones)
    else:
        if iteraciones == 0:
            p.prueba_indef(N)
        else:
            p.prueba_def(N, iteraciones)

if __name__ == "__main__":
    args: list[str] = sys.argv[1:]

    if len(args) > 3:
        print('Muchos argumentos...')
        print('Para usar el programa ejecuta uv run main.py N, ITERACIONES, s/n')
        print('Si ITERACIONES es 0, ')

    if len(args) == 2:
        main(*verificar_input(*args))

    if len(args) == 3:
        main(*verificar_input(*args))
