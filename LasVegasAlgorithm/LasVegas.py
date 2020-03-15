import random
import time

def quicksort(arr, start , stop):
    if(start < stop):
        pivotindex = partitionrand(arr, start, stop)
        quicksort(arr , start , pivotindex - 1)
        quicksort(arr, pivotindex + 1, stop)

def partitionrand(arr , start, stop):
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)

def partition(arr,start,stop):
    pivot = start
    i = start + 1
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)

f = open('randomInts/random_10000.txt', 'r')
x = f.read().splitlines()
f.close()

for i in range(len(x)):
    x[i] = int(x[i])

start_time = time.time()
quicksort(x, 0, len(x)-1)
end_time = time.time() - start_time
print(x)
print('----- %s seconds -----' % end_time)
