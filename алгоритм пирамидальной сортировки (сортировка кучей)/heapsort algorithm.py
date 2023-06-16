def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считается корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — это допустимый индекс, а элемент больше,
    # чем текущий наибольший, то мы обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # То же самое и для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент уже не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    # Создаём Max Heap из списка
    # 2-й аргумент означает остановку алгоритма перед элементом -1, то есть
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении,
    # уменьшая счётчик i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в самый конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


# Проверяем, что всё работает
random_list_of_nums = [99, 1.3, 1.2, 3, 5, 6, 8.2, 8, 9]
heap_sort(random_list_of_nums)
print('Отсортированный список:', random_list_of_nums)


# def heapsort(alist):
#     build_max_heap(alist)
#     for i in range(len(alist) - 1, 0, -1):
#         alist[0], alist[i] = alist[i], alist[0]
#         max_heapify(alist, index=0, size=i)
#
#
# def parent(i):
#     return (i - 1) // 2
#
#
# def left(i):
#     return 2 * i + 1
#
#
# def right(i):
#     return 2 * i + 2
#
#
# def build_max_heap(alist):
#     length = len(alist)
#     start = parent(length - 1)
#     while start >= 0:
#         max_heapify(alist, index=start, size=length)
#         start = start - 1
#
#
# def max_heapify(alist, index, size):
#     l = left(index)
#     r = right(index)
#     if (l < size and alist[l] > alist[index]):
#         largest = l
#     else:
#         largest = index
#     if (r < size and alist[r] > alist[largest]):
#         largest = r
#     if (largest != index):
#         alist[largest], alist[index] = alist[index], alist[largest]
#         max_heapify(alist, largest, size)
#
#
# alist = input('введите целые числа, через запятую: ').split()
# alist = [int(x) for x in alist]
# heapsort(alist)
# print('отсортированный список: ', end='')
# print(alist)
