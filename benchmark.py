
from data import load_data, save_json
from files import TIMES_FILE
import time
import sorts
import sys
from tqdm import tqdm


def run_bench():

    # it reaches the recursion limit, so I increase it
    sys.setrecursionlimit(1_000_000)
    bench_data = load_data()

    sort_algorithms = {
        'Bubble sort': sorts.bubble_sort,
        'Selection sort': sorts.selection_sort,
        'Insertion sort': sorts. insertion_sort,
        'Shell sort': sorts.shell_sort,

        'Quick sort': sorts.quick_sort,
        'Merge sort': sorts.merge_sort,
        'Heap sort': sorts.heap_sort,

    }

    times = []
    for data in tqdm(bench_data):
        for name, algorithm in sort_algorithms.items():
            copy_data = data.copy()
            sorted_array = copy_data.copy()
            sorted_array.sort()
            assert sorted_array != copy_data
            start = time.time()
            algorithm(copy_data)
            stop = time.time()
            dt = stop - start
            times.append((name, len(data), dt))

    save_json(TIMES_FILE, times)


if __name__ == "__main__":
    run_bench()
