# для слияния списков
def merge(a1, a2):
    c = []
    i = j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            c.append(a1[i])
            i+=1
        else:
            c.append(a2[j])
            j+=1
    # добавляем недостающие элементы
    c+= a1[i:] + a2[j:]
    return c
    
# для сортировки слиянием
def split_and_merge(arr):
    n = len(arr) // 2
    a1 = arr[:n]
    a2 = arr[n:]
    
    if len(a1) > 1:
        a1 = split_and_merge(a1)
    if len(a2) > 1:
        a2 = split_and_merge(a2)
    
    return merge(a1, a2)
    
n = int(input())

nums = list(map(int, input().split()))

print(*split_and_merge(nums), end = ' ')
