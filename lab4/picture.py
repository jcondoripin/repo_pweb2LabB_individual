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
        return Picture(vertical)

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
        imgConcat = []
        for value in range(len(self.img)):
            strConcat = self.img[value] * n
            imgConcat.append(strConcat)
        return Picture(imgConcat)

    def verticalRepeat(self, n):
        imgConcat = []
        for i in range(n):
            for value in range(len(self.img)):
                strConcat = self.img[value]
                imgConcat.append(strConcat)
        return Picture(imgConcat)

    #Extra: Sólo para realmente viciosos 
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""
        newImg = []
        for i in range(len(self.img)): 
            filaImg = ""
            for value in self.img[::-1]: # horario
                filaImg += value[i]
            newImg.append(filaImg)
        return Picture(newImg)
    
    def replace(self, p):
        """Devuelve una figura cuyos espacios vacíos sean reemplazados por los
        espacios de la figura pasada"""
        newImg = []
        for i in range(len(self.img)):
            newValue = ""
            for j in range(len(self.img[i])):
                if self.img[i][j] == " ":
                    newValue += p.img[i][j]
                else:
                    newValue += self.img[i][j]
            newImg.append(newValue)
        return Picture(newImg)
            

