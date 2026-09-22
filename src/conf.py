condiciones_feromonas: dict[str, float] = {
    'tau_min': 0.05,
    'rho': 0.67,
    'alpha': 1,
    'beta': 3
}

macro_condiciones: dict[str, int] = {
    'micro_iteraciones': 400,
    'pruebas_por_tablero': 2,
    'N_inicial': 4
}

type Coord = tuple[int, int]
