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
from unittest.mock import patch
from pessoa import Pessoa # type: ignore

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('glauco', 'campos')
        self.p2 = Pessoa('luiz', 'carlos')
    
    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(
            self.p1.nome,
            'glauco',
        )
        self.assertEqual(
            self.p2.nome,
            'luiz',
        )

    def test_pessoa_attr_nome_deve_ser_str(self):
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)

    def test_pessoa_attr_sobrenome_deve_ser_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(
            self.p1.sobrenome,  
            'campos',
        )
        self.assertEqual(
            self.p2.sobrenome,  
            'carlos',
        )

    def test_pessoa_attr_dados_obtidos_inicia_com_o_valor_false(self):
        self.assertFalse(self.p1.dados_obtidos)
        self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obterTodosOsDados(), 'conectado')
            self.assertTrue(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obterTodosOsDados(), 'conectado')
            self.assertTrue(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_falha_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obterTodosOsDados(), 'falha')
            self.assertFalse(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obterTodosOsDados(), 'falha')
            self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obterTodosOsDados(), 'conectado')
            self.assertTrue(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obterTodosOsDados(), 'conectado')
            self.assertTrue(self.p2.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obterTodosOsDados(), 'falha')
            self.assertFalse(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obterTodosOsDados(), 'falha')
            self.assertFalse(self.p2.dados_obtidos)

if __name__ == '__main__':
    unittest.main(verbosity=2)