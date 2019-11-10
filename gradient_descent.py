import cost_function as cf

class GradienDescent:
    def __init__(self, alpha):
        self.alpha = alpha

    def calculate(self, data_set, theta):
        temptheta = theta[:]
        thetaZero, thetaOne = temptheta
        data = data_set[:]
        tempThetaZero = thetaZero - (self.alpha * float(self.thetaZeroSummation(data, thetaZero, thetaOne) / len(data)) ) 
        tempThetaOne = thetaOne - (self.alpha * float(self.thetaOneSummation(data, thetaZero, thetaOne) / len(data)) )
        costf = cf.CostFunction(thetaZero, thetaOne)
        error = costf.calculate(data)
        print("ThetaZero: {}".format(tempThetaZero))
        print("ThetaOne: {}".format(tempThetaOne))
        print("Error: {}".format(error))
        input("Halt")
        return self.calculate(data, [tempThetaZero, tempThetaOne])

    def thetaZeroSummation(self, data_set, thetaZero, thetaOne):
        out = 0
        for dataX, dataY in data_set:
            out += thetaZero + (thetaOne * dataX) - dataY
        #print("thetaZeroSummation: {}".format(out))
        return out

    def thetaOneSummation(self, data_set, thetaZero, thetaOne):
        out = 0
        for dataX, dataY in data_set:
            out += (thetaZero + (thetaOne * dataX) - dataY) * dataX
        #print("thetaOneSummation: {}".format(out))
        return out

def testCompile():
    gd = GradienDescent(alpha=0.1)
    data_set = [
    (1,1),
    (2,2),
    (3,3)
    ]
    thetaZero=0
    thetaOne=0.9
    theta = [thetaZero, thetaOne]
    gd.calculate(data_set, theta)
    print(thetaZero, thetaOne)

testCompile()