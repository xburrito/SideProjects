import NeuralNetwork as neuralNet
import os.path
from os import path


# if file already exist then load datasets from external files
if (path.exists("TrainingDataset400.txt") and path.exists("TestingDataset200.txt")):
    print("\nLoading datasets from external file (totalSize = 600)...")
    #load training and testing dataset from external txt file
    trainingDataset = neuralNet.loadDatasetFromFile("TrainingDataset400.txt")
    testingDataset = neuralNet.loadDatasetFromFile("TestingDataset200.txt")
else: # if file doesn't exist then generate the datasets and write it on a file
    print("\nGenerating Training Datasets (totalSize = 600)...")
    # Generate training Dataset (totalsize = 400)
    datasetH200 =  neuralNet.generateH(200)
    datasetL200 = neuralNet.generateL(200)
    trainingDataset = [datasetH200, datasetL200]
    # Generate testing Dataset (totalSize = 200)
    datasetH100 = neuralNet.generateH(100)
    datasetL100 = neuralNet.generateL(100)
    testingDataset = [datasetH100, datasetL100]

    # write datasets into external txt file
    neuralNet.writeDatasetIntoFile("TrainingDataset400.txt", trainingDataset)
    neuralNet.writeDatasetIntoFile("TestingDataset200.txt", testingDataset)


print("\nPrinting Training Dataset...")
# print training Dataset
neuralNet.printDatasetArrays(trainingDataset)
print("\nPrinting Testing Dataset...")
# print testing Dataset
neuralNet.printDatasetArrays(testingDataset)

# verify size of training and testing dataset
print("\nSize of Generated Datasets")
print("Training dataset = ", len(trainingDataset[0]) + len(trainingDataset[1]))
print("Testing dataset = ", len(testingDataset[0]) + len(testingDataset[1]))

# OPTIONAL: displays dataset "images"
#print("\nDatasets image representation...")
#neuralNet.displayImages(trainingDataset[0])
#neuralNet.displayImages(trainingDataset[1])
#neuralNet.displayImages(testingDataset[0])
#neuralNet.displayImages(testingDataset[1])

# 1D index of array
I = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# number of indices inside tuples
n = 3
#  number of tuples inside J
m = 4
# generate random indices
J = neuralNet.generateJlist(m, n, I)

# create 4 empty arrays for H and L
# [ 0,  1,  2,  3,  4,  5,  6,  7]
# [000,001,010,011,100,101,110,111]

T1h = [0, 0, 0, 0, 0, 0, 0, 0]
T2h = [0, 0, 0, 0, 0, 0, 0, 0]
T3h = [0, 0, 0, 0, 0, 0, 0, 0]
T4h = [0, 0, 0, 0, 0, 0, 0, 0]
T1l = [0, 0, 0, 0, 0, 0, 0, 0]
T2l = [0, 0, 0, 0, 0, 0, 0, 0]
T3l = [0, 0, 0, 0, 0, 0, 0, 0]
T4l = [0, 0, 0, 0, 0, 0, 0, 0]

trainingData = [[T1h, T2h, T3h, T4h], [T1l, T2l, T3l, T4l]]  # = 200

# invoke train neural network
print("\n\nTraining the Neural Network!.....\n")
neuralNet.train(trainingDataset, J, trainingData)

# Visualize the data collected
print("\nData Collected:")
print(" 0,  1,  2,  3,  4,  5,  6,  7")
print("000 001 010 011 100 101 110 111")
print("-------------------------------")
neuralNet.visualizeTrainingData(trainingData)

print("\n\nTesting the Neural Network!...\n")
neuralNet.test(testingDataset, J, trainingData)


# 30 Points Bonus: Adjust that value for n iterations (increase/decrease) based on the performance.
print("\n\n30 Points Bonus: observing how modifying the value by a variable affects the accuracy!")
n=20 # number of iterations
variable = 0.5 # initial value
print("n =", n)
print("initial value for variable =", variable,"\n")
input("Press Enter to continue...")

for i in range(n):
    print("n = ", i+1)
    print("variable =", round(variable, 2))
    # generate random indices
    J = neuralNet.generateJlist(m, 3, I)
    # invoke experimental test
    neuralNet.experimentalTest(testingDataset, J, trainingData, variable)
    #neuralNet.visualizeTrainingData(trainingData)
    variable += 0.1 # modify variable after each iteration
    print("----------------")