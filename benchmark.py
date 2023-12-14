
from data import load_data, save_json
from files import TIMES_FILE
import time
import sorts
import sys

sys.setrecursionlimit(1_000_000)


def run_bench():

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

    times: dict[str, float] = {}
    for i, data in enumerate(bench_data):
        print(f'running: {i+1}-{len(bench_data)}, data size: {len(data)}')
        for name, algorithm in sort_algorithms.items():
            start = time.time()
            algorithm(data)
            stop = time.time()
            times[name] = stop - start

    save_json(TIMES_FILE, times)
