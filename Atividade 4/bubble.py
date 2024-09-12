def median(arr):
    if not arr:
        raise ValueError("O vetor está vazio")
    
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    mid = n // 2
    
    if n % 2 == 1:
        return sorted_arr[mid]
    else:
        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
