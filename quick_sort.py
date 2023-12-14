def quick_sort(a: list[int]) -> None:

    def swap(i: int, j: int):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def partition(low: int, high: int) -> int:
        pivot_value = a[high]
        pivot_index = low - 1

        for i in range(low, high):

            if a[i] <= pivot_value:
                pivot_index += 1
                swap(pivot_index, i)

        pivot_index +=1
        swap(pivot_index, high)
        return pivot_index 

    def _sort(low: int, high: int):

        if low >= high:
            return
        pivot = partition(low, high)
        _sort(low, pivot - 1)
        _sort(pivot + 1, high)

    size = len(a)
    low = 0
    high = size - 1

    _sort(low, high)
