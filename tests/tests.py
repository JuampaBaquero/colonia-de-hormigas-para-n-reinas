import unittest
import numpy as np
from src import Conflictos, Hormiga, Feromonas

class Pruebas(unittest.TestCase):
    def test_poner_una_reina_a_conflictear_4x4(self) -> None:
        conflictos: Conflictos = Conflictos(4)
        conflictos.reinear((0, 2))
        np.testing.assert_array_equal(conflictos.matriz, 
                                      [[1, 1, -1, 1],
                                       [0, 1,  1, 1],
                                       [1, 0,  1, 0],
                                       [0, 0,  1, 0]])

    def test_hormigas_calcular_heuristica(self) -> None:
        array_in: list[int] = [0, 1, 2, 3]
        array_out: list[float] = [1, 0.5, 0.3333333, 0.25]
        conflictos: Conflictos = Conflictos(4)
        feromonas: Feromonas = Feromonas(4, rho=0.4)
                
        hormiga: Hormiga = Hormiga(4, conflictos, feromonas)

        heu_test: np.ndarray = hormiga._Hormiga__heuristica(np.array(array_in)) # type: ignore
        np.testing.assert_almost_equal(heu_test, np.array(array_out))

    def test_hormigas_prob_correcta(self) -> None:
        conflictos: Conflictos = Conflictos(4)
        feromonas: Feromonas = Feromonas(4, rho = 0.4, tau_min = 0)

        feromonas.matriz[0, 2] = 1

        hormiga: Hormiga = Hormiga(4, conflictos, feromonas)

        posicion_resultado: tuple = hormiga._Hormiga__elegir_posicion_prob(0) #type: ignore

        self.assertIn(posicion_resultado, [(0, 1), (0, 2), (0, 3), (0, 4)])

    def test_poner_reinas(self) -> None:
        conflictos: Conflictos = Conflictos(4)
        feromonas: Feromonas = Feromonas(4, rho=0.4, tau_min = 0)
        
        hormiga: Hormiga = Hormiga(4, conflictos, feromonas)

        feromonas.matriz[0, 1] = 1
        feromonas.matriz[1, 3] = 1
        feromonas.matriz[2, 0] = 1
        feromonas.matriz[3, 2] = 1

        hormiga.poner_reinas()

        self.assertEqual(int(conflictos.matriz[0, 1]), -1)
        self.assertEqual(int(conflictos.matriz[1, 3]), -1)
        self.assertEqual(int(conflictos.matriz[2, 0]), -1)
        self.assertEqual(int(conflictos.matriz[3, 2]), -1)

    def test_pillarse_conflictos_globales(self) -> None:
        conflictos: Conflictos = Conflictos(4)
        feromonas: Feromonas = Feromonas(4, rho=0.4, tau_min = 0)        
        hormiga: Hormiga = Hormiga(4, conflictos, feromonas)

        hormiga.reinas.extend([(0, 0), (3, 0), (0, 3), (2, 2)])

        """
        Este caso es este:

        * . . *
        . . . .
        . . * .
        * . . .

        Deberían haber 4 conflictos...
        """
        res: int = hormiga._Hormiga__conflictos_globales() # type: ignore
        self.assertEqual(res, 4)

if __name__ == '__main__':
    unittest.main()