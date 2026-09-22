import os
import re
import numpy as np
from conf import Coord, condiciones_feromonas, macro_condiciones
from Ciclo import Ciclo

class Pruebas:

    @staticmethod
    def imprimir_tablero(N: int, coordenadas: list[Coord]) -> None:
        tablero: np.ndarray = np.full((N, N), '☐')
        for pos in coordenadas:
            tablero[pos] = '♛'

        print(tablero)
    
    @staticmethod
    def prueba_def(N: int, iteraciones: int, imprimir: bool = True) -> tuple[float, int]:

        print(f'[PRUEBA_DEF] probando con tablero {N}x{N}, con {iteraciones} iteraciones')
        ciclo: Ciclo = Ciclo(N, **condiciones_feromonas)
        tiempo, (sol_optima, conflictos, coordenadas) = ciclo.ciclar(iteraciones) #type: ignore

        if imprimir:
            print(f'=== CICLANDO {iteraciones} ITERACIONES ===')
            ciclo: Ciclo = Ciclo(N, **condiciones_feromonas)
            tiempo, (sol_optima, conflictos, coordenadas) = ciclo.ciclar(iteraciones) #type: ignore

            print(f'Las hormigas {'SI' if sol_optima else 'NO'} alcanzaron una solución óptima\n')
            print(f'Hay {conflictos} conflictos')
            print(f'El tablero es: ')
            Pruebas.imprimir_tablero(N, coordenadas) # type: ignore
            print(f'La ejecución se demoró: {tiempo}')

            return tiempo, conflictos 

        else:
            print(f'[TERMINADA] prueba finalizada con éxito: (t = {tiempo}, conf = {conflictos})')
            return tiempo, conflictos

    @staticmethod
    def prueba_indef(N: int, imprimir: bool = True) -> tuple[float, int]:
        print(f'[PRUEBA_INDEF] probando con un tablero {N}x{N}...')
        ciclo: Ciclo = Ciclo(N, **condiciones_feromonas)
        tiempo, (iteraciones, coordenadas) = ciclo.ciclar_indef() #type: ignore

        if imprimir:
            print(f'Las hormigas alcanzaron una solución óptima en {iteraciones} pasos')
            print(f'El tablero es: ')
            Pruebas.imprimir_tablero(N, coordenadas) # type: ignore
            print(f'Las hormigas se demoraron: {tiempo}s')

            return(tiempo, iteraciones) #type: ignore

        else:
            print(f'[TERMINADA] prueba finalizada con éxito: (t = {tiempo}, it = {iteraciones})')
            return tiempo, iteraciones #type: ignore

    @staticmethod
    def probar_n_tableros(N: int, iteraciones: int) -> None:

        if iteraciones == 0:
            for i in range(macro_condiciones['N_inicial'], N + 1):
                for _ in range(macro_condiciones['pruebas_por_tablero']):

                    tiempo, intentos = Pruebas.prueba_indef(i, False)
                    Pruebas.guardar_indef(i, intentos, tiempo, micro_iteraciones = macro_condiciones['micro_iteraciones'], **condiciones_feromonas)

        else:
            for i in range(macro_condiciones['N_inicial'], N + 1):
                for _ in range(macro_condiciones['pruebas_por_tablero']):
                    
                    tiempo, conflictos = Pruebas.prueba_def(i, iteraciones, False)
                    Pruebas.guardar_def(i, iteraciones, tiempo, conflictos)

    @staticmethod
    def guardar_indef(N: int, intentos: int, tiempo: float, alpha: float, beta: float, 
                      tau_min: float, rho: float, micro_iteraciones: int) -> None:

        """
        Nota curiosa: Esta función la hice a mano para que guardara una muestra, quería que guardara también un archivo
        con los parámetros, pero me daba pereza hacerla 
        FUE LA ÚNICA FUNCIÓN QUE VIBE CODEÉ y por hacerlo, se me embarró la lógica de lo que quería hacer
        Así que lo siguiente es solo por flojo, para corregir un path que la IA hizo mal...
        """

        ruta_muestra: str = 'output/muestra_2.csv' #Cambiar esto según la muestra que estés haciendo... 
        #Disculparasme lo rudimentario pero me da pereza corregir lo que hizo gemi
        
        dir_output: str = 'output'
        os.makedirs(dir_output, exist_ok=True)
        ruta_parametros = os.path.join(dir_output, 'parametros.csv')

        ultimo_n: int = 0
        for archivo in os.listdir(dir_output):
            match = re.match(r'muestra_(\d+)\.csv', archivo)
            if match:
                n_arch = int(match.group(1))
                if n_arch > ultimo_n:
                    ultimo_n = n_arch

        numero_archivo = ultimo_n if ultimo_n > 0 else 1
        es_nuevo_archivo = False

        if os.path.exists(ruta_parametros):
            with open(ruta_parametros, 'r', encoding='utf-8') as f:
                lineas = f.readlines()
                if len(lineas) > 1:
                    ultima_linea = lineas[-1].strip().split(',')
                    try:
                        last_n = int(ultima_linea[0])
                        last_alpha = float(ultima_linea[1])
                        last_beta = float(ultima_linea[2])
                        last_tau_min = float(ultima_linea[3])
                        last_rho = float(ultima_linea[4])
                        last_micro = int(ultima_linea[5])

                        if (last_alpha != alpha or last_beta != beta or
                            last_tau_min != tau_min or last_rho != rho or
                            last_micro != micro_iteraciones):
                            numero_archivo = ultimo_n + 1
                            es_nuevo_archivo = True
                        else:
                            numero_archivo = last_n
                    except (ValueError, IndexError):
                        numero_archivo = ultimo_n + 1
                        es_nuevo_archivo = True
        else:
            es_nuevo_archivo = True
            if ultimo_n > 0:
                numero_archivo = ultimo_n + 1

        if es_nuevo_archivo or (numero_archivo == 1 and not os.path.exists(ruta_parametros)):
            modo = 'a' if os.path.exists(ruta_parametros) else 'w'
            with open(ruta_parametros, modo, encoding='utf-8') as f:
                if modo == 'w':
                    f.write('numero_archivo,alpha,beta,tau_min,rho,micro_iteraciones\n')
                f.write(f'{numero_archivo},{alpha},{beta},{tau_min},{rho},{micro_iteraciones}\n')

        archivo_nuevo = not os.path.exists(ruta_muestra)

        with open(ruta_muestra, 'a', encoding='utf-8') as f:
            if archivo_nuevo:
                f.write('N,INTENTOS,TIEMPO\n')
            f.write(f'{N},{intentos},{tiempo:.4f}\n')

    @staticmethod
    def guardar_def(N: int, intentos: int, tiempo: float, conflictos: int) -> None:

        ruta_archivo: str = 'output/output_def.csv'
        archivo_nuevo: bool = not os.path.exists(ruta_archivo)
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

        with open(ruta_archivo, 'a', encoding='utf-8') as f:
            if archivo_nuevo:
                f.write('N,INTENTOS,TIEMPO,CONFLICTOS\n')

            f.write(f'{N},{intentos},{tiempo:.4f}, {conflictos}\n')