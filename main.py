import time
import json
import random
from pathlib import Path

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from quick_sort import quick_sort
from merge_sort import merge_sort, sys
from heap_sort import heap_sort

DATA_FILE = Path('bench_data.json')
TIMES_FILE = Path('times.json')


def load_data() -> list[list[int]]:
    bytes = DATA_FILE.read_bytes()
    json_ref = json.loads(bytes)

    return list(json_ref)


def create_data() -> list[list[int]]:
    bench_data = [create_random_array(i) for i in range(1_00, 101_00, 1_00)]
    return bench_data


def create_random_array(size: int) -> list[int]:
    max_int = 10_000
    return [random.randint(-max_int, max_int) for _ in range(size)]


def test_algorithm():
    data = create_data()

    test_data = data[0]
    assert_data = test_data.copy()

    heap_sort(test_data)

    assert_data.sort()

    assert len(test_data) == len(assert_data)
    assert test_data == assert_data, f'Result:{test_data}\nExpected:{assert_data}'
    print('passed')


def run_bench():

    if not DATA_FILE.exists():
        bench_data = create_data()
        save_json(DATA_FILE, bench_data)
    else:
        bench_data = load_data()

    sort_algorithms = {
        'Bubble sort': bubble_sort,
        'Selection sort': selection_sort,
        'Insertion sort': insertion_sort,
        'Shell sort': shell_sort,

        'Quick sort': quick_sort,
        'Merge sort': merge_sort,
        'Heap sort': heap_sort,

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


def save_json(file_path: Path, data) -> None:
    print(f'saving {file_path}')
    json_string = json.dumps(data)
    file_path.write_text(json_string)


def main():
    sys.setrecursionlimit(1_000_000)
    run_bench()


if __name__ == "__main__":
    main()
