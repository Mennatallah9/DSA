''' recursive binary search
Time complexity: O(log(n))
Space complexity: O(log(n)) '''

def binarySearch(arr, target):
    def helper(left, right):
        if left>right:
            return -1
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return helper(mid+1, right)
        else:
            return helper(left, mid-1)
    return helper(0, len(arr)-1)

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