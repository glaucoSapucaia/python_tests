'''
TDD -> Test driven development (Iniciando códigos com TESTES)

Red
1. Criar o teste e ver FALHAR.

Green
2. Criar o código e ver o teste PASSAR.

Refactor
3. MELHORAR o código.
'''
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
from bacon import _bacon # type: ignore

class TestBacon(unittest.TestCase):
    def test_bacon_levanta_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            _bacon('0')

    def test_bacon_deve_retornar_ba_e_com_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'bacon'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(_bacon(entrada), saida, msg=f'{entrada} não retornou {saida}')

    def test_bacon_deve_retornar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7)
        saida = 'fome'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(_bacon(entrada), saida, msg=f'{entrada} não retornou {saida}')

    def test_bacon_deve_retornar_ba_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12)
        saida = 'ba'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(_bacon(entrada), saida, msg=f'{entrada} não retornou {saida}')

    def test_bacon_deve_retornar_con_se_entrada_for_multiplo_de_5(self):
        entradas = (5, 10, 20, 25)
        saida = 'con'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(_bacon(entrada), saida, msg=f'{entrada} não retornou {saida}')

if __name__ == '__main__':
    unittest.main(verbosity=2)