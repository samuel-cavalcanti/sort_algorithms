def bubble_sort(a: list[int]) -> None:
    size = len(a)

    def swap(i: int, j: int):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def run_bubble() -> bool:
        swapped = False
        for i in range(size-1):
            if a[i] > a[i+1]:
                swap(i, i+1)
                swapped = True
        return swapped

    swapped = run_bubble()
    while swapped:
        swapped =run_bubble()


    return None
