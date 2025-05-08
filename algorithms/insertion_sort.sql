def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[ j - 1], arr[j] = arr[j], arr[j - 1]
                
            else:
                break
        print(' '.join(map(str, arr[:i + 1])))
        # print()
    return arr


n = int(input())



nums = list(map(int, input().split()))

insertion_sort(nums)
