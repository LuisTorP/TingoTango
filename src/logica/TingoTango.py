class TingoTango():
    def textoTingoTango(self,numero):
        if (numero % 3 == 0):
            return 'Tingo'
        if (numero % 5 ==0):
            return 'Tango'
        if ((numero % 5 == 0) and (numero % 3 ==0)):
            return 'TingoTango'