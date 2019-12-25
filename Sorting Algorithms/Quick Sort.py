# Libraries used
import random
import time

def quickSort(arr_list):
  quickSortHelper(arr_list,0,len(arr_list)-1)

def quickSortHelper(arr_list,first,last):
  if first<last:

    splitpoint = partition(arr_list,first,last)

    quickSortHelper(arr_list,first,splitpoint-1)
    quickSortHelper(arr_list,splitpoint+1,last)


def partition(arr_list,first,last):

  # Pivot value is set to the first index of the array
  piv_val = arr_list[first]

  left = first+1
  right = last

  completed = False
  while not completed:

    # Checks to make sure the left index values are smaller than the pivot value
    # Check every left index value to make sure that it is smaller than the right
    while left <= right and arr_list[left] <= piv_val:
      left = left + 1

    # Checks to make sure the right index values are greater than the pivot value
    # Check every right index value to make sure that it is larger than the left
    while arr_list[right] >= piv_val and right >= left:
      right = right -1

    if right < left:
      completed = True
    else:

      # Swap function performed if left index value is greater than the right index value
      temp = arr_list[left]
      arr_list[left] = arr_list[right]
      arr_list[right] = temp

  # Swap function
  temp = arr_list[first]
  arr_list[first] = arr_list[right]
  arr_list[right] = temp

  return right

def quickSortDriver(x):
  arr = []
  for i in range(x): # Size of the array
    n = random.randint(0,1000) # Every value in array is between 0 - 1000
    arr.append(n)
    quickSort(arr)
  print(arr)
  print("")
  print("Time taken to run a quick sort with pivot set to first index: ")

start_time = (time.time() * (10**3)) #Converting from seconds to milliseconds

arr_size = int(input("What is the array size you are trying to sort: "))
quickSortDriver(arr_size)

print("%s milliseconds" % ((time.time() * (10**3)) - start_time))
print("")
