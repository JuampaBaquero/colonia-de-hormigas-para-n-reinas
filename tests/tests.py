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
        conflictos: Conflictos = Conflictos(4)
        feromonas: Feromonas = Feromonas(4, rho=0.4)
                
        hormiga: Hormiga = Hormiga(4, conflictos, feromonas)

        heu_1: float = hormiga.heuristica(0)
        heu_2: float = hormiga.heuristica(1)
        heu_3: float = hormiga.heuristica(3)

        self.assertAlmostEqual(heu_1, 1)
        self.assertAlmostEqual(heu_2, 0.5)
        self.assertAlmostEqual(heu_3, 0.25)

    def test_hormigas_prob_correcta(self) -> None:
        conflictos: Conflictos = Conflictos(4)
        feromonas: Feromonas = Feromonas(4, rho = 0.4, tau_0 = 0)

        feromonas.matriz[0, 2] = 1

        hormiga: Hormiga = Hormiga(4, conflictos, feromonas)

        resulting = hormiga.calcular_mayor_prob(0)

        self.assertEqual(resulting, (0, 2))

    def test_poner_reinas(self) -> None:
        conflictos: Conflictos = Conflictos(4)
        feromonas: Feromonas = Feromonas(4, rho=0.4, tau_0 = 0)
        
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

if __name__ == '__main__':
    unittest.main()