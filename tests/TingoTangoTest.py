import unittest
from src.logica.TingoTango import TingoTango

class TingoTangoPrueba(unittest.TestCase):
    def setUp(self):
        self.TT=TingoTango()

    def tearDown(self):
        self.TT=None

    def test_TingoTango_multiploTres_retornaTingo(self):
        # Arrange
            self.numero=6
            self.resultadoEsperado = 'Tingo'
        # Do
            self.resultadoActual = self.TT.textoTingoTango (self.numero)
        # Assert
            self.assertEqual (self.resultadoEsperado, self.resultadoActual)