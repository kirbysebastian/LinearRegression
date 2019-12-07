'''
----DESCRIPTION HERE!----

TODO LIST:
 - Fix CostFunction to support multivariable inputs
 - Fix GradientDescent to support multivariable inputs
 - Fix GradientChecking to support multivariable inputs
 - Add description
 - Structurize the project
 - Create Tests for each class
'''
import sys
sys.setrecursionlimit(10**6)

class Hypothesis:
    __bias = []
    __theta = []

    def __init__(self, theta):
        self.__bias = [sample[0] for sample in theta]
        self.__theta = [sample[1:] for sample in theta]
        #print("Calculated - Bias: {}\nCalculated - Slope: {}\n".format(self.__bias, self.__theta))

    def calculate(self, dataX):
        # hypos = []
        # for i, x in enumerate(dataX):
        #     sum_x = 0
        #     for j, x_val in enumerate(x):
        #         sum_x += self.__theta[i][j] * x_val
        #     hypos.append(self.__bias[i] + sum_x)

        hypos = [
            self.__bias[i] + sum(
                [self.__theta[i][j] * x_val
                for j, x_val in enumerate(x)]
            )
            for i, x in enumerate(dataX)
        ]

        #print("Calculated Hypothesis: {}\n".format(hypos))
        return hypos

    def getSlope(self):
        return self.__theta

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
        #thetaZero, thetaOne = temptheta
        data = data_set[:]

        # theta0Gradient = self.thetaZeroSummation(data, thetaZero, thetaOne) / len(data)
        # theta1Gradient = self.thetaOneSummation(data, thetaZero, thetaOne) / len(data)

        # print("Actual gradient values, ZERO: {}, ONE: {}".format(theta0Gradient, theta1Gradient))
        # gc = GradientChecking()
        # approxGradThetaZero = gc.thetaZeroGradApprox(data, thetaZero, thetaOne)
        # approxGradThetaOne = gc.thetaOneGradApprox(data, thetaZero, thetaOne)
        # print("Approx gradient values, ZERO: {}, ONE: {}".format(approxGradThetaZero, approxGradThetaOne))
        # thetaZeroError = (theta0Gradient / approxGradThetaZero) * 100
        # thetaOneError = (theta1Gradient / approxGradThetaOne) * 100
        # print("Gradient Accuracy, ZERO: {}%, ONE: {}%".format(thetaZeroError, thetaOneError))

        # tempThetaZero = thetaZero - (self.learning_rate * theta0Gradient) 
        # tempThetaOne = thetaOne - (self.learning_rate * theta1Gradient)
        # error = CostFunction(thetaZero, thetaOne).calculate(data)
        # print("ThetaZero: {}".format(tempThetaZero))
        # print("ThetaOne: {}".format(tempThetaOne))
        # print("Error: {}".format(error))

        # input("Halt")

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

class GradientChecking:
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
    def __init__(self, trainX, trainY):
        self.model = []
        self.trainX = trainX[:]
        self.trainY = trainY[:]

        bias = self.calculateBias(trainX[:], trainY[:])

        # Defaults theta=1 - to change
        self.theta = [
            [1 if i > 0 else bias for i in range(len(x)+1)]
            for x in self.trainX
        ]
        #print(self.theta)

        self.hypothesis = Hypothesis(self.theta[:]).calculate(self.trainX)        
        # for i, sample in enumerate(self.theta):
        #     print("Calculated Theta-sample({}): {}".format(i, sample))

    def calculateBias(self, trainX, trainY):
        x = trainX[0]
        y = trainY[0]
        b = y
        for val in x:
            b -= val
        return b

    def train(self, learning_rate: float):
        self.gd = GradientDescent(learning_rate)
        #trainX.insert(0, 1)
        

        

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