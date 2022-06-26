# def binary_search(list, num):
#     first = 0
#     last = len(list) - 1
#     while first <= last:
#         middle = (first + last) // 2
#         if list[middle] == num:
#             return f'данный элемент находится под индекс {middle}'
#         elif list[middle] > num:
#             last = middle - 1
#         elif list[middle] < num:
#             first = middle + 1
#     return f'элемент не найден'
#
#
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14]
# result = binary_search(list, 10)
# print(f'Result: {result}')

def selection_sort(lst):
    for i in range (len(lst)):
        min_value = i
        for j in range (i, len(lst)):
            if lst[min_value] > lst[j]:
                min_value = j
        lst[i],lst[min_value] = lst[min_value], lst[i]
    return lst


list = [1, 19, 3, 4, 56, 6, 7, 8, 9, 10, 15,2,13,14]
print(list)
result = selection_sort(list)
print(f'Result: {result}')

