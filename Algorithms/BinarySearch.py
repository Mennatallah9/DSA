''' iterative binary search
Time complexity: O(log(n))
Space complexity: O(1) '''

def binarySearch(arr, target):
    left, right = 0, len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 # target not found

# test
if __name__=="__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5
    print(binarySearch(arr, target)) # 4
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target = 5
    print(binarySearch(arr, target)) # -1
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target = 100
    print(binarySearch(arr, target)) # 9
