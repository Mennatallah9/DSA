''' Bubble Sort Algorithm
Time Complexity: O(n^2)
Space Complexity: O(1)
'''
def BubbleSort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break
    return arr

# test
if __name__=="__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(BubbleSort(arr)) # [11, 12, 22, 25, 34, 64, 90]
    arr = [5, 1, 4, 2, 8]
    print(BubbleSort(arr)) # [1, 2, 4, 5, 8]
    arr = [1, 2, 3, 4, 5]
    print(BubbleSort(arr)) # [1, 2, 3, 4, 5]
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(BubbleSort(arr)) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    print(BubbleSort(arr)) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    arr = [1, 3, 2, 4, 5]
    print(BubbleSort(arr)) # [1, 2, 3, 4, 5]
    arr = [1, 2, 3, 5, 4]
    print(BubbleSort(arr)) # [1, 2, 3, 4, 5]
    arr = [1, 2, 3, 4, 5, 6]
    print(BubbleSort(arr)) # [1, 2, 3, 4, 5, 6]
    arr = [6, 5, 4, 3, 2, 1]
    print(BubbleSort(arr)) # [1, 2, 3, 4, 5, 6]
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(BubbleSort(arr)) # [1, 2, 3, 4, 5, 6, 7]