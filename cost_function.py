import hypothesis as h

class CostFunction:
    def __init__(self, thetaZero, thetaOne):
        self.h = h.Hypothesis(thetaZero, thetaOne)

    def squared_summation(self, data_set):
        sumSquared = 0
        for dataX, dataY in data_set:
            sumSquared += self.squared(float(self.h.calculate(dataX) - dataY))
        return sumSquared

    def squared(self, dataInput):
        return dataInput * dataInput

    def calculate(self, data_set):
        out = self.squared_summation(data_set) / (2 * len(data_set))
        #print("CostFunction: {}".format(out))
        return out









################################################
def testCompile():
    cf = CostFunction(thetaZero=0, thetaOne=5)
    data_set = [
    (1,1),
    (2,2),
    (3,3)
    ]
    data_set2 = [
    (1,-890),
    (2,-1411),
    (2,-1560),
    (3,-2220),
    (3,-2091),
    (4,-2878),
    (5,-3537),
    (6,-3268),
    (6,-3920),
    (6,-4163),
    (8,-5471),
    (10,-5157),
    ]
    cf.calculate(data_set)

#testCompile()