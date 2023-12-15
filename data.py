
import random
from files import DATA_FILE,  save_json, load_json


def load_data() -> list[list[int]]:
    if not DATA_FILE.exists():
        print('creating data')
        bench_data = create_data()
        save_json(DATA_FILE, bench_data)
        return bench_data

    json_data = load_json(DATA_FILE)
    return list(json_data)


def create_data() -> list[list[int]]:
    bench_data = [create_random_array(i) for i in range(1_00, 10_000, 100)]
    return bench_data


def create_random_array(size: int) -> list[int]:
    max_int = 10_000
    return [random.randint(-max_int, max_int) for _ in range(size)]
