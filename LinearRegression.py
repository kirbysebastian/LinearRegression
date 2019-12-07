'''
----DESCRIPTION HERE!----

TODO LIST:
 - todo 1
 - todo 2
 - todo 3
'''
import sys
sys.setrecursionlimit(10**6)

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
        return out

    def getSlope(self):
        return self.__slope


class CostFunction:
    def __init__(self, thetaZero, thetaOne):
        self.h = Hypothesis(thetaZero, thetaOne)

    def squared_summation(self, data_set):
        sumSquared = 0
        for dataX, dataY in data_set:
            sumSquared += self.squared(float(self.h.calculate(dataX) - dataY))
        return sumSquared

    def squared(self, dataInput):
        return dataInput * dataInput

    def calculate(self, data_set):
        out = self.squared_summation(data_set) / (2 * len(data_set))
        return out


class GradientDescent:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    def calculate(self, data_set, theta):
        temptheta = theta[:]
        thetaZero, thetaOne = temptheta
        data = data_set[:]

        theta0Gradient = self.thetaZeroSummation(data, thetaZero, thetaOne) / len(data)
        theta1Gradient = self.thetaOneSummation(data, thetaZero, thetaOne) / len(data)
        print("Actual gradient values, ZERO: {}, ONE: {}".format(theta0Gradient, theta1Gradient))
        gc = GradientChecking()
        approxGradThetaZero = gc.thetaZeroGradApprox(data, thetaZero, thetaOne)
        approxGradThetaOne = gc.thetaOneGradApprox(data, thetaZero, thetaOne)
        print("Approx gradient values, ZERO: {}, ONE: {}".format(approxGradThetaZero, approxGradThetaOne))
        thetaZeroError = (theta0Gradient / approxGradThetaZero) * 100
        thetaOneError = (theta1Gradient / approxGradThetaOne) * 100
        print("Gradient Accuracy, ZERO: {}%, ONE: {}%".format(thetaZeroError, thetaOneError))

        tempThetaZero = thetaZero - (self.learning_rate * theta0Gradient) 
        tempThetaOne = thetaOne - (self.learning_rate * theta1Gradient)
        error = CostFunction(thetaZero, thetaOne).calculate(data)
        print("ThetaZero: {}".format(tempThetaZero))
        print("ThetaOne: {}".format(tempThetaOne))
        print("Error: {}".format(error))

        input("Halt")

        # if error < 0.0008:
        #     tempThetaZero = int(round(tempThetaZero))
        #     tempThetaOne = int(round(tempThetaOne))
        #     print("Error reached threshold. Removing floating theta values.")
        #     print("\ntempThetaZero: {}, tempThetaOne: {}".format(tempThetaZero, tempThetaOne))

        return self.calculate(data, [tempThetaZero, tempThetaOne])

    def thetaZeroSummation(self, data_set, thetaZero, thetaOne):
        out = 0
        for dataX, dataY in data_set:
            out += ( thetaZero + (thetaOne * dataX) - dataY )
        #print("thetaZeroSummation: {}".format(out))
        return out

    def thetaOneSummation(self, data_set, thetaZero, thetaOne):
        out = 0
        for dataX, dataY in data_set:
            out += ( (thetaZero + (thetaOne * dataX) - dataY) * dataX )
        #print("thetaOneSummation: {}".format(out))
        return out

class GradientChecking():
    def __init__(self):
        self.epsilon = 0.0001

    def thetaZeroGradApprox(self, data, thetaZero, thetaOne):
        costPlus = CostFunction(thetaZero+self.epsilon, thetaOne).calculate(data)
        costMinus = CostFunction(thetaZero-self.epsilon, thetaOne).calculate(data)

        return ( (costPlus - costMinus) / (2*self.epsilon) )

    def thetaOneGradApprox(self, data, thetaZero, thetaOne):
        costPlus = CostFunction(thetaZero, thetaOne+self.epsilon).calculate(data)
        costMinus = CostFunction(thetaZero, thetaOne-self.epsilon).calculate(data)

        return ( (costPlus - costMinus) / (2*self.epsilon) )

class LinearRegression:
    def __init__(self):
        self.model = []

    def train(self, learningRate: float, trainX: list, trainY: list):
        self.gd = GradienDescent(learningRate)
        

# def testCompile():
#     gd = GradienDescent(learning_rate=0.0006, epochs=10)
#     data_set = generateData(100)
#     thetaZero=5
#     thetaOne=1
#     theta = [thetaZero, thetaOne]
#     gd.calculate(data_set, theta)
#     print(thetaZero, thetaOne)

# testCompile()
#print(generatedData(10))