# Libraries used
import random
import time

def insertionSort(arr):
  # Traverse from 1 to size of array
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

# Insertion sort Driver Code
def insertionSortDriver(x):
  arr = []
  for i in range(x): # Size of the array
    n = random.randint(0,1000) # Every value in array is between 0 - 1000
    arr.append(n)
    insertionSort(arr)
  print(arr)
  print("")
  print("Time taken to run an insertion sort: ")

start_time = (time.time() * (10**3)) #Converting from seconds to milliseconds

arr_size = int(input("What is the array size you are trying to sort: "))
insertionSortDriver(arr_size)

print("%s milliseconds" % ((time.time() * (10**3)) - start_time))
print("")
