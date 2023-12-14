import sys


def merge_sort(a: list[int]) -> None:

    def _split(begin: int, end: int):
        if end - begin <= 1:
            return

        split_size = (end + begin) // 2
        _split(begin, split_size)
        _split(split_size, end)
        _merge(begin, end, split_size)

    def _merge(begin: int, end: int, split_size: int):
        left = a[begin:split_size]
        right = a[split_size:end]
        # Quando acabar os elementos, de um dos arranjos
        # a comparação current_right <= current_left, sempre irá para o outro arranjo
        # que possui elementos, pois left[-1] ou right[-1] == infinito
        left.append(sys.maxsize)
        right.append(sys.maxsize)
        right_index = 0
        left_index = 0

        current_left = left[left_index]
        current_right = right[right_index]

        for i in range(begin, end):
            if current_left <= current_right:
                a[i] = current_left
                left_index += 1
                current_left = left[left_index]
            else:
                a[i] = current_right
                right_index += 1
                current_right = right[right_index]

    _split(begin=0, end=len(a))
