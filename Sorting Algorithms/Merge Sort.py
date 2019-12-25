# Libraries used
import random
import time

def mergeSort(arr):
  if len(arr) > 1:

    # Locates the middle of the array
    mid = len(arr)//2

    # Splits the arrays into 2 sub-arrays
    L = arr[:mid]
    R = arr[mid:]

    # mergeSort calls itself to sort the left sub-array followed by the right sub-array
    mergeSort(L)
    mergeSort(R)
    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i+=1
      else:
        arr[k] = R[j]
        j+=1
      k+=1

    # Checking if any element was left
    while i < len(L):
      arr[k] = L[i]
      i+=1
      k+=1

    while j < len(R):
      arr[k] = R[j]
      j+=1
      k+=1

# Merge sort Driver Code
def mergeSortDriver(x):
  arr = []

  # Parameter takes in size of array
  for i in range(x):
    # Every value in array is between 0 - 1000
    n = random.randint(0,1000)
    arr.append(n)
    mergeSort(arr)
  print(arr)
  print("")
  print("Time taken to run a merge sort: ")

start_time = (time.time() * (10**3)) # Converting from seconds to milliseconds

arr_size = int(input("What is the array size you are trying to sort: "))
mergeSortDriver(arr_size)

print("%s milliseconds" % ((time.time() * (10**3)) - start_time))
print("")
