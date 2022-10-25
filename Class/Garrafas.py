class Garrafa:
    def __init__(self, vMax, vNow):
        self.vMax = vMax
        self.vNow = vNow

    def llenar(self):
        self.vNow = self.vMax

    def vaciar(self):
        self.vNow = 0

    def setVNow(self, vNow):
        self.vNow = vNow

    def getVMax(self):
        return self.vMax

    def getVNow(self):
        return self.vNow