from colors import *
class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = []
        for value in self.img:
    	    vertical.append(value[::-1])
        return vertical

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        horizontal = []
        for value in self.img[::-1]:
            horizontal.append(value)
        return Picture(horizontal)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        inverter = []
        for value in self.img:
            strInverter = ""
            for char in value:
                strInverter = strInverter + self._invColor(char)
            inverter.append(strInverter)
        return Picture(inverter)

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        imgConcat = []
        for value in range(len(self.img)):
            strConcat = self.img[value] + p.img[value]
            imgConcat.append(strConcat)
        return Picture(imgConcat)

    def up(self, p):
        imgConcat = []
        for value in p.img:
            imgConcat.append(value)
        for value in self.img:
            imgConcat.append(value)
        return Picture(imgConcat)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        imgConcat = []
        for value in self.img:
            imgConcat.append(value)
        for value in p.img:
            imgConcat.append(value)
        return Picture(imgConcat)
    
    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        return Picture(None)

    def verticalRepeat(self, n):
        return Picture(None)

    #Extra: Sólo para realmente viciosos 
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""
        return Picture(None)
