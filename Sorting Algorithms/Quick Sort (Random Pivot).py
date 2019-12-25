# Libraries used
import random
import time

def quickSortRandomPivot(arr_list):
  quickSortHelperRandomPivot(arr_list,0,len(arr_list)-1)

def quickSortHelperRandomPivot(arr_list,first,last):
  if first < last:

    splitpoint = partitionRandomPivot(arr_list,first,last)

    quickSortHelperRandomPivot(arr_list,first,splitpoint-1)
    quickSortHelperRandomPivot(arr_list,splitpoint+1,last)

def partitionRandomPivot(arr_list,first,last):
  # Pivot value is chosen at random from any value between the first and last of the array (last value inclusive)
  piv_val = arr_list[random.randrange(first, last+1, 1)]

  left = first+1
  right = last

  done = False
  while not done:

    # Checks to make sure the left index values are smaller than the pivot value
    # Check every left index value to make sure that it is smaller than the right
    while left <= right and arr_list[left] <= piv_val:
      left = left + 1

    # Checks to make sure the right index values are greater than the pivot value
    # Check every right index value to make sure that it is larger than the left
    while arr_list[right] >= piv_val and right >= left:
      right = right -1

    if right < left:
      done = True
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

def quickSortRandomPivotDriver(x):
  arr = []
  for i in range(x): # Size of the array
    n = random.randint(0,1000) # Every value in array is between 0 - 1000
    arr.append(n)
    quickSortRandomPivot(arr)
  print(arr)
  print("")
  print("Time taken to run a quick sort at a random pivot: ")

start_time = (time.time() * (10**3)) #Converting from seconds to milliseconds

arr_size = int(input("What is the array size you are trying to sort: "))
quickSortRandomPivotDriver(arr_size)

print("%s milliseconds" % ((time.time() * (10**3)) - start_time))
print("")
