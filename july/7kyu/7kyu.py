def smaller(arr):
    n = len(arr)
    res = [0] * n
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                res[i] += 1
    
    return res