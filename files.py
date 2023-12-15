import json
from pathlib import Path
from typing import Any, Optional

TIMES_FILE = Path('times.json')
DATA_FILE = Path('bench_data.json')


def save_json(file_path: Path, data) -> None:
    print(f'saving {file_path}')
    json_string = json.dumps(data)
    file_path.write_text(json_string)


def load_json(file_path: Path) -> Any:
    print(f'loading {file_path}')
    data_bytes = file_path.read_bytes()
    json_ref = json.loads(data_bytes)
    return json_ref


def load_time_data() -> Optional[list[tuple[str, int, float]]]:
    if not TIMES_FILE.exists():
        return None
    json_data = load_json(TIMES_FILE)
    return list(json_data)
