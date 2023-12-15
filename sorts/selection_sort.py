def selection_sort(a: list[int]) -> None:
    size = len(a)

    def find_min(start_index: int):
        min = start_index
        for i in range(start_index, size):
            if a[i] < a[min]:
                min = i
        return min

    def swap(i: int, j: int):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    for i in range(size):
        min_index = find_min(start_index=i)

        if min_index != i:
            swap(min_index, i)

    return None