from pathlib import Path

BASE_DIR = Path(__file__).parent


def get_sequence_prediction(seq: list[int]) -> int:
    seqs = [seq]
    last_seq = seq
    while not all([x == 0 for x in last_seq]):
        last_seq = [last_seq[x + 1] - last_seq[x] for x in range(0, len(last_seq) - 1)]
        seqs.append(last_seq)
    value = 0
    for s in reversed(seqs):
        value += s[-1]
    return value


def get_sequence_ancestor(seq: list[int]) -> int:
    seqs = [seq]
    last_seq = seq
    while not all([x == 0 for x in last_seq]):
        last_seq = [last_seq[x + 1] - last_seq[x] for x in range(0, len(last_seq) - 1)]
        seqs.append(last_seq)
    value = 0
    for s in reversed(seqs):
        value = s[0] - value
    return value


def question_1(data: str) -> int:
    sequences = [[int(x) for x in line.split()] for line in data.splitlines()]
    res = 0
    for sequence in sequences:
        res += get_sequence_prediction(sequence)

    return res


def question_2(data: str) -> int:
    sequences = [[int(x) for x in line.split()] for line in data.splitlines()]
    res = 0
    for sequence in sequences:
        res += get_sequence_ancestor(sequence)

    return res


def test_question_1():
    data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
    res = question_1(data)
    assert res == 114


def test_question_2():
    data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
    res = question_2(data)
    assert res == 2


if __name__ == "__main__":
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
