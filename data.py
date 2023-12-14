
import random
from pathlib import Path
import json
from files import DATA_FILE


def load_data() -> list[list[int]]:
    if not DATA_FILE.exists():
        bench_data = create_data()
        save_json(DATA_FILE, bench_data)
        return bench_data

    bytes = DATA_FILE.read_bytes()
    json_ref = json.loads(bytes)

    return list(json_ref)


def create_data() -> list[list[int]]:
    bench_data = [create_random_array(i) for i in range(1_00, 101_00, 1_00)]
    return bench_data


def create_random_array(size: int) -> list[int]:
    max_int = 10_000
    return [random.randint(-max_int, max_int) for _ in range(size)]


def save_json(file_path: Path, data) -> None:
    print(f'saving {file_path}')
    json_string = json.dumps(data)
    file_path.write_text(json_string)
