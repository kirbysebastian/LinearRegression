class Hypothesis:
    __origin = 0
    __slope = 0

    def __init__(self, thetaZero, thetaOne):
        self.thetaZero = thetaZero
        self.thetaOne = thetaOne
        self.__origin = self.thetaZero
        self.__slope = self.thetaOne

    def calculate(self, dataInputX):
        out = self.__origin + (self.__slope * dataInputX)
        #print("Hypothesis: {}".format(out))
        return out

    def getSlope(self):
        return self.__slope














######################################################
def testCompile():
    h = Hypothesis(0, 0)
    h.calculate(0)

#testCompile()