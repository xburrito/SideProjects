import random

# variation indices for H and L
hVariations = [(3, 8), (7,8), (8,9), (7,9),(4,5),(4,6),(5,4),(5,6)]
lVariations = [(1,4), (7,10), (11,12),(1,12),(4,11),(3,11),(3,8,12,4),(2,5,8,11)]

# Generates dataset for class H
def generateH(size):
    # temp dataset
    datasetH = []
    # loop "size" times
    for _ in range(size):
        # create default H "image"
        H = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
        # add noise to default "image" by selecting a random variation (tuple) for H
        variation = hVariations[random.randint(0, len(hVariations) - 1)]
        # iterate selected (tuple)
        for i in range(len(variation)):
            # set random int at current index
            H[variation[i] - 1] = random.randint(0, 1)
        # append array "image" into list
        datasetH.append(H)
    return datasetH

# Generates dataset for class L
def generateL(size):
    # temp dataset
    datasetL = []
    # loop "size" times
    for _ in range(size):
        # create default L "image"
        L = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1]
        # add noise to default "image" by selecting a random variation (tuple) for L
        # since the tuple for L contains only one item, it treats it as an int not as a tuple, hence this code
        variation = lVariations[random.randint(0, len(lVariations) - 1)]
        # iterate selected (tuple)
        for i in range(len(variation)):
            # set random int at current index
            L[variation[i] - 1] = random.randint(0, 1)
        # append array "image" into list
        datasetL.append(L)
    return datasetL

# write dataset into an external txt file
def writeDatasetIntoFile(filePath, dataset):
    # open or create file if it doesn't exist
    file = open(filePath, "w+")
    # iterate rows
    for i in range(len(dataset)):
        if (i == 0):
            file.write("Class H\n")
        else:
            file.write("Class L\n")
        # iterate columns
        for j in range(len(dataset[i])):
            # convert whole list into a string
            str1 = ', '.join(str(e) for e in dataset[i][j])
            # write string (list) into file
            file.write("[" + str1 + "]\n")
    file.close()

# loads dataset from external txt file
def loadDatasetFromFile(filePath):
    dataset = [[],[]] # --> [[H],[L]]
    flag = False
    file = open(filePath, "r")
    file.readline().rstrip('\n') # "removes" H line"

    while True:
        # read line
        line = file.readline().rstrip('\n')

        # check if line is not empty
        if not line:
            break # exit
        elif line.__contains__("L"):
            line = file.readline().rstrip('\n')  # "skips" L line
            flag = True

        # format line and add convert into a list
        list = line.replace("[","").replace("]","").split(", ")
        list = [int(i) for i in list]

        if flag: # add line to L list
            dataset[1].append(list)
        else: # add line to H list
            dataset[0].append(list)
    #printDatasetA
    file.close()
    return dataset

# displays the dataset "images"
def displayImages(array):
    # iterate "row"
    for i in range(len(array)):
        print("\n")  # create a new line
        counter = 0
        # iterate "column"
        for j in range(len(array[i])):
            if (counter == 3):
                print("", end="\n")  # create a new line
                counter = 0  # reset counter
            if (array[i][j] == 1):
                print(" #", end="")  # print on same line
            else:
                print("  ", end="")  # print on same line
            counter += 1;  # increase counter

# displays the Dataset "arrays"
def printDatasetArrays(trainingDataset):
    # iterate rows
    for i in range(len(trainingDataset)):
        if (i == 0):
            print("Class H")
        else:
            print("Class L")
        # iterate columns
        for j in range(len(trainingDataset[i])):
            # print array in each column
            print(trainingDataset[i][j])

# generate a list of m tuples with n random indices in each tuple
def generateJlist(m, n, I):
    # temp J
    J = []
    # shuffle indices
    random.shuffle(I)
    counter = 0
    # create "m" lists
    for _ in range(m):
        tmpList = []
        # add "n" random tuples into lists
        for _ in range(n):
            tmpList.append(I[(counter)])
            counter += 1 # increment, points to next index
        # convert list into tuple and add it into J
        J.append(tuple(tmpList))
    return J

# generate S list
def generateSlist(J, H):
    # temp S
    S = []
    # iterate J rows
    for i in range(len(J)):
        tmpList = []
        # iterate J columns (tuples)
        for j in range(len(J[i])):
            index = (J[i][j]) # select index from tuple
            # given index select value (0 or 1) from H
            value = H[index-1] # index-1, since H index starts from zero
            # add value into list
            tmpList.append(value)
        # convert list into tuple and add it into S
        S.append(tuple(tmpList))
    return S

# converts binary to decimal
def binaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

# trains the neural network
def train(trainingDataset, J, trainingData):
    # iterate rows of trainingDataset
    for i in range(len(trainingDataset)):
        # iterate columns (array of tuples) of trainingDataset
        for j in range(len(trainingDataset[i])):
            # get current Class H or L based on i
            currentClass = trainingDataset[i][j]
            # generate S list based on J
            S = generateSlist(J, currentClass)

            # iterate rows of S list to populate the 4 columns (arrays) in trainingData
            for k in range(len(S)):
                binary = ""
                # iterate columns (tuples) of S list
                for l in range(len(S[k])):
                    # convert each value (1 or 0) of tuple into string and
                    # append it into binary string
                    binary += str(S[k][l])
                # convert binary(pattern) into decimal index
                index = binaryToDecimal(int(binary))
                # increment occurrence of tuple (pattern) at its specified index
                trainingData[i][k][index] += 1;


# Displays the data collected after training
def visualizeTrainingData(trainingData):
    # iterate rows
    for i in range(len(trainingData)):
        if (i == 1):
            print("Class H:")
        else:
            print("Class L:")
            # iterate columns
        for j in range(len(trainingData[i])):
            # print array in each column
            print(trainingData[i][j])


# tests the neural network
def test(testingDataset, J,  trainingData):
    # returns actual corresponding class when invoked
    getActualClass = lambda x: "H" if x == 0 else "L"
    # returns predicted class when invoked
    getPrediction = lambda x, y: "H" if x > y else "L"

    correct = 0;
    incorrect = 0

    # iterate rows of testingDataset
    for i in range(len(testingDataset)):
        # iterate columns (array of tuples) of testingDataset
        for j in range(len(testingDataset[i])):
            # get current Class H or L based on i
            currentClass = testingDataset[i][j]
            # generate S list based on J
            S = generateSlist(J, currentClass)

            # iterate rows of S list to calculate the sum
            # of patterns (tuples) from the 8 columns (arrays) in trainingData
            for k in range(len(S)):
                totalSumH = 0
                totalSumL = 0

                binary = ""
                # iterate columns (tuples) of S list
                for l in range(len(S[k])):
                    # convert each value (1 or 0) of tuple into string and
                    # append it into binary string
                    binary = binary + str(S[k][l])
                # convert binary(pattern) into decimal index
                index = binaryToDecimal(int(binary))

                # get values from trainingDataset and add them to their respective sums
                totalSumH += trainingData[0][k][index]; # from H
                totalSumL += trainingData[1][k][index]; # from L

            # invoke lambda functions to get actual class and prediction
            prediction = getPrediction(totalSumH,totalSumL)
            actualClass = getActualClass(i)

            if(prediction == actualClass):
                bool = True
                correct += 1
            else:
                bool = False
                incorrect += 1
            print(currentClass, "Actual Class:", actualClass, "Predicted Class:", prediction, bool)
    probability = correct/(correct+incorrect) * 100
    print("\nAccuracy:", probability, "%")


# --- 30 Points Bonus ----

# EXPERIMENTAL test
def experimentalTest(testingDataset, J,  trainingData, variable):
    # returns actual corresponding class when invoked
    getActualClass = lambda x: "H" if x == 0 else "L"
    # returns predicted class when invoked
    getPrediction = lambda x, y: "H" if x > y else "L"

    correct = 0;
    incorrect = 0

    # iterate rows of testingDataset
    for i in range(len(testingDataset)):
        # iterate columns (array of tuples) of testingDataset
        for j in range(len(testingDataset[i])):
            # get current Class H or L based on i
            currentClass = testingDataset[i][j]
            # generate S list based on J
            S = generateSlist(J, currentClass)

            # iterate rows of S list to calculate the sum
            # of patterns (tuples) from the 8 columns (arrays) in trainingData
            for k in range(len(S)):
                totalSumH = 0
                totalSumL = 0

                binary = ""
                # iterate columns (tuples) of S list
                for l in range(len(S[k])):
                    # convert each value (1 or 0) of tuple into string and
                    # append it into binary string
                    binary = binary + str(S[k][l])
                # convert binary(pattern) into decimal index
                index = binaryToDecimal(int(binary))

                # get values from trainingDataset and add them to their respective sums
                totalSumH += trainingData[0][k][index]; # from H
                totalSumL += trainingData[1][k][index]; # from L

            # invoke lambda functions to get actual class and prediction
            prediction = getPrediction(totalSumH,totalSumL)
            actualClass = getActualClass(i)

            if(prediction == actualClass):
                bool = True
                correct += 1
                # increase value of tuple occurrences
                modifyValue(trainingData, i, S, variable)
            else:
                bool = False
                incorrect += 1
                # decrease value of tuple occurrences
                modifyValue(trainingData, i, S, (variable * -1))
            #print(currentClass, "Actual Class:", actualClass, "Predicted Class:", prediction, bool)
    probability = correct/(correct+incorrect) * 100
    print("Accuracy:", probability, "%")


#  increase or decrease array values, based on given variable
def modifyValue(trainingData, image, S, variable):
    # iterate rows (tuples) in S
    for i in range(len(S)):
        binary = ""
        # iterate columns (values) in tuples
        for l in range(len(S[i])):
            binary = binary + str(S[i][l])
        # convert binary(pattern) into decimal index
        index = binaryToDecimal(int(binary))
        # increment corresponding tuple value by new variable
        trainingData[image][i][index] += variable;