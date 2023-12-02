from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).parent


def question_1(data: str) -> Any:
    ...


def question_2(data: str) -> Any:
    ...


def test_question_1():
    data = """"""
    res = question_1(data)
    assert res is None


def test_question_2():
    data = """"""
    res = question_2(data)
    assert res is None


if __name__ == "__main__":
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
