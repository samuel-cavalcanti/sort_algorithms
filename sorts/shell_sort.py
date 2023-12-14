def shell_sort(a: list[int]) -> None:

    size = len(a)
    gap = _find_initial_gap(size)

    def swap(i: int, j: int):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def insert(i: int, gap: int):
        for index in range(i+gap, 0, -gap):
            if a[index] < a[index - gap]:
                swap(index - gap, index)

    while gap > 0:

        for i in range(0, size - gap):
            insert(i, gap)

        gap = gap // 2


def _find_initial_gap(size: int):
    gap = 1
    while gap < size:
        gap = gap*3 + 1

    return gap // 3
