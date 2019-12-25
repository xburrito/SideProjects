# Libraries used
import random
import time

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
  largest = i # Initialize largest as root
  l = 2 * i + 1     # left = (2 * i) + 1
  r = 2 * i + 2     # right = (2 * i) + 2

  # Checks if left child of root exists and is greater than the root
  if l < n and arr[i] < arr[l]:
    largest = l

  # Checks if right child of root exists and is greater than root
  if r < n and arr[largest] < arr[r]:
    largest = r

  # Change root, if needed
  if largest != i:
    arr[i],arr[largest] = arr[largest],arr[i] # swap

    # Heapify the root
    heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
  n = len(arr)

  # Build a maxheap.
  for i in range(n, -1, -1):
    heapify(arr, n, i)

  # One by one extract elements
  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i] # swap
    heapify(arr, i, 0)

# Heap sort Driver Code
def heapSortDriver(x):
  arr = []
  for i in range(x): # Size of the array
    n = random.randint(0,1000) # Every value in array is between 0 - 1000
    arr.append(n)
    heapSort(arr)
  print(arr)
  print("")
  print("Time taken to run a heapsort: ")

start_time = (time.time() * (10**3)) #Converting from seconds to milliseconds

arr_size = int(input("What is the array size you are trying to sort: "))
heapSortDriver(arr_size)

print("%s milliseconds" % ((time.time() * (10**3)) - start_time))
print("")
