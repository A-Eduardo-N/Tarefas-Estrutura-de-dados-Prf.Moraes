#Questão 1
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encontre o menor elemento no subarray não ordenado
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Troque o menor elemento encontrado com o primeiro elemento do subarray não ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#Questão 2
def custom_sort(arr, order='asc'):
    if order == 'asc':
        return selection_sort(arr)
    elif order == 'desc':
        arr = selection_sort(arr)
        return arr[::-1]  # Reverte a lista para ordem decrescente
    else:
        raise ValueError("Parâmetro 'order' deve ser 'asc' ou 'desc'")

#Questão 3
def find_max_min(arr):
    if not arr:
        raise ValueError("O vetor está vazio")
    
    max_element = arr[0]
    min_element = arr[0]
    
    for num in arr[1:]:
        if num > max_element:
            max_element = num
        if num < min_element:
            min_element = num
    
    return max_element, min_element

#Questão 4
def second_smallest(arr):
    if len(arr) < 2:
        raise ValueError("O vetor deve ter pelo menos dois elementos")
    
    unique_sorted_arr = sorted(set(arr))
    if len(unique_sorted_arr) < 2:
        raise ValueError("Não há um segundo menor número único")
    
    return unique_sorted_arr[1]

#Questão 5
def remove_duplicates(arr):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
    return result

#Questão 6
def sort_and_count_even_odd(arr):
    sorted_arr = sorted(arr, reverse=True)
    even_count = sum(1 for num in sorted_arr if num % 2 == 0)
    odd_count = len(sorted_arr) - even_count
    return sorted_arr, even_count, odd_count

#Questão 7
def third_largest(arr):
    if len(arr) < 3:
        raise ValueError("O vetor deve ter pelo menos três elementos")
    
    unique_sorted_arr = sorted(set(arr), reverse=True)
    if len(unique_sorted_arr) < 3:
        raise ValueError("Não há um terceiro maior número único")
    
    return unique_sorted_arr[2]

#Questão 8
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
