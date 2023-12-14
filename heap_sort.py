def heap_sort(a: list[int]) -> None:

    build_max_heap(a)

    size = len(a)

    for i in range(size-1, 0, -1):
        __swap(a, 0, i)
        size -= 1
        heapify(heap=a, current_index=0, heap_size=size)


def build_max_heap(a: list[int]):

    size = len(a)
    for i in range(size//2, -1, -1):
        heapify(a, i, size)


def heapify(heap: list[int], current_index: int, heap_size: int):
    l = __left(current_index)
    r = __right(current_index)
    if l < heap_size and heap[l] > heap[current_index]:
        high = l
    else:
        high = current_index

    if r < heap_size and heap[r] > heap[high]:
        high = r

    if current_index != high:
        __swap(heap, current_index, high)
        heapify(heap, high, heap_size)


def __left(i: int) -> int:
    return 2*i + 1


def __right(i: int) -> int:
    return 2*(i + 1)


def __swap(heap: list[int], i: int, j: int):
    temp = heap[i]
    heap[i] = heap[j]
    heap[j] = temp
