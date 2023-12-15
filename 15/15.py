from pathlib import Path
from collections import OrderedDict

BASE_DIR = Path(__file__).parent


def compute_hash(s: str) -> int:
    res = 0
    for c in s:
        res = (res + ord(c)) * 17 % 256
    return res


def question_1(data: str) -> int:
    res = 0
    for s in data.split(","):
        res += compute_hash(s.strip())
    return res


def question_2(data: str) -> int:
    boxes = OrderedDict()
    for i in range(256):
        boxes[i] = OrderedDict()
    for op in data.split(","):
        op = op.strip()
        if op.endswith("-"):
            label = op[:-1]
            box = compute_hash(label)
            if label in boxes[box]:
                del boxes[box][label]
        else:
            label, focal_length = op.split("=")
            box = compute_hash(label)
            boxes[box][label] = focal_length
    res = 0
    for k in sorted(boxes.keys()):
        for slot, focal_length in enumerate(boxes[k].values()):
            res += (k + 1) * (slot + 1) * int(focal_length)
    return res


def test_compute_hash():
    data = "HASH"
    res = compute_hash(data)
    assert res == 52
    assert compute_hash("rn") == 0
    assert compute_hash("cm") == 0
    assert compute_hash("qp") == 1


def test_question_1():
    data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
    res = question_1(data)
    assert res == 1320


def test_question_2():
    data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
    res = question_2(data)
    assert res == 145


if __name__ == "__main__":
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
