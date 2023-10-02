def sum_negative_elements(lst):
    negative_sum = sum([num for num in lst if num < 0])
    return negative_sum

def sum_elements_between_zeros(lst):
    first_zero_index = None
    second_zero_index = None

    for i, num in enumerate(lst):
        if num == 0:
            if first_zero_index is None:
                first_zero_index = i
            elif second_zero_index is None:
                second_zero_index = i
                break

    if first_zero_index is None or second_zero_index is None:
        return 0

    elements_between_zeros = lst[first_zero_index + 1:second_zero_index]
    elements_sum = sum(elements_between_zeros)
    return elements_sum

lst = list(map(int,input('Введите лист ').split()))
print("Сумма отрицательных элементов:", sum_negative_elements(lst))
print("Сумма элементов между двумя первыми нулями:", sum_elements_between_zeros(lst))