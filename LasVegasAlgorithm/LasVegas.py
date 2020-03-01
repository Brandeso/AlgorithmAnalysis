import random

def partition(arr, low, high):
    i = (low-1)
    randn = random.randInt(low,high+1)
    pivot = arr[randn]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[randn] = arr[randn],arr[i+1]
    return(i+1)

def quickSort(arr, low, high)
    if low < high:
        pi = partition(arr, low, high):
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
