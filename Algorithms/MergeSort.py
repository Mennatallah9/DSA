'''
Time complexity: O(nlogn)
Space complexity: O(n)
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    l, r = 0, 0 # left and right indices
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    # if there are elements left in left or right
    res.extend(left[l:])
    res.extend(right[r:])
    return res


# test
if __name__=="__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(arr)) # [3, 9, 10, 27, 38, 43, 82]
    arr = [38, 27, 43, 3, 9, 82, 10, 1]
    print(merge_sort(arr)) # [1, 3, 9, 10, 27, 38, 43, 82]
    arr = [38, 27, 43, 3, 9, 82, 10, 1, 100]
    print(merge_sort(arr)) # [1, 3, 9, 10, 27, 38, 43, 82, 100]