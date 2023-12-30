import unittest
from calculator import soma

class TestCalculator(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(
            soma(5, 5), 10
        )

    def test_soma_10_e_5_deve_retornar_15(self):
        self.assertEqual(
            soma(10, 5),
            15
        )

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (100, 100, 200),
            (110, 110, 220),
            (130, 10, 140),
            (10, -10, 0),
        )
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida= x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(
                    soma(x, y),
                    saida,
                )

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertion_error(self):
        with self.assertRaises(AssertionError):
            soma('10', 20)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertion_error(self):
        with self.assertRaises(AssertionError):
            soma(20, '20')

unittest.main(verbosity=2)