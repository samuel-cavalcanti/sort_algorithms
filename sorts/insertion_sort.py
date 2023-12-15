def insertion_sort(a: list[int]) -> None:
    size = len(a)

    def move_itens_to_left(index: int, value: int) -> int:
        while index >= 0 and value < a[index]:
            a[index+1] = a[index]
            index -= 1
        return index

    def insert(index: int, value: int):
        a[index] = value

    for i in range(1, size):
        current_item = a[i]
        last_index = move_itens_to_left(i-1, current_item)

        if last_index != i:
            insert(last_index + 1, current_item)