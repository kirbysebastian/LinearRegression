from LinearRegression import LinearRegression

def generateLinearFunction(dataX, intercept):
    return [i[0]+intercept for i in dataX]

def generateFunction(dataX, bias):
    y_list = []
    for x_data in dataX:
        x_sum = 0
        for x in x_data:
            x_sum += x
        y_list.append(x_sum)
    return y_list
    #return [intercept+x for x in xList for xList in dataX]

def main():

    num_of_examples = 3

    # Single Variable
    x = [[i] for i in range(1, num_of_examples+1)]
    # y = x
    y = generateFunction(x, bias=0)
    print("Examples:\n X--> {}\n Y--> {}\n".format(x, y))

    lr = LinearRegression(x, y)
    lr.train(learning_rate=0.001)
    











if __name__ == '__main__':
    main()