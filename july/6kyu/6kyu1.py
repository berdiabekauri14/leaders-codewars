def sum_nested_numbers(arr):
    total = 0
    for element in arr:
        if isinstance(element, arr):
            total += sum_nested_numbers(element)
        else:
            total += element
    return total