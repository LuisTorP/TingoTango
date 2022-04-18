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

    def test_TingoTango_multiploCinco_retornaTango(self):
        # Arrange
            self.numero=5
            self.resultadoEsperado = 'Tango'
        # Do
            self.resultadoActual = self.TT.textoTingoTango (self.numero)
        # Assert
            self.assertEqual (self.resultadoEsperado, self.resultadoActual)

    def test_TingoTango_multiploQuince_retornaTingoTango(self):
        # Arrange
            self.numero=15
            self.resultadoEsperado = 'TingoTango'
        # Do
            self.resultadoActual = self.TT.textoTingoTango (self.numero)
        # Assert
            self.assertEqual (self.resultadoEsperado, self.resultadoActual)