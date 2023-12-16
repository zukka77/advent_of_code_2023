from pathlib import Path

BASE_DIR = Path(__file__).parent


# 0=up 1=left 2=down 3=right
def run_ray(start: tuple[int, int], field: list[list[str]], direction: int) -> set[tuple[int, int, int]]:
    r = start[0]
    c = start[1]
    seen = set()
    pos = set([(r, c, direction)])
    while pos:
        r, c, d = pos.pop()
        if (r >= 0 and r < len(field)) and (c >= 0 and c < len(field[0])) and (r, c, d) not in seen:
            seen.add((r, c, d))
            if d == 0:
                if field[r][c] in (".", "|"):
                    pos.add((r - 1, c, d))
                    continue
                if field[r][c] == "/":
                    pos.add((r, c + 1, 3))
                    continue
                if field[r][c] == "\\":
                    pos.add((r, c - 1, 1))
                    continue
                if field[r][c] == "-":
                    pos.add((r, c - 1, 1))
                    pos.add((r, c + 1, 3))
                    continue
                assert False
            if d == 3:
                if field[r][c] in (".", "-"):
                    pos.add((r, c + 1, d))
                    continue
                if field[r][c] == "/":
                    pos.add((r - 1, c, 0))
                    continue
                if field[r][c] == "\\":
                    pos.add((r + 1, c, 2))
                    continue
                if field[r][c] == "|":
                    pos.add((r - 1, c, 0))
                    pos.add((r + 1, c, 2))
                    continue
                assert False
            if d == 1:
                if field[r][c] in (".", "-"):
                    pos.add((r, c - 1, d))
                    continue
                if field[r][c] == "/":
                    pos.add((r + 1, c, 2))
                    continue
                if field[r][c] == "\\":
                    pos.add((r - 1, c, 0))
                    continue
                if field[r][c] == "|":
                    pos.add((r + 1, c, 2))
                    pos.add((r - 1, c, 0))
                    continue
                assert False
            if d == 2:
                if field[r][c] in (".", "|"):
                    pos.add((r + 1, c, d))
                    continue
                if field[r][c] == "/":
                    pos.add((r, c - 1, 1))
                    continue
                if field[r][c] == "\\":
                    pos.add((r, c + 1, 3))
                    continue
                if field[r][c] == "-":
                    pos.add((r, c - 1, 1))
                    pos.add((r, c + 1, 3))
                    continue
                assert False
            assert False
    return seen


def question_1(data: str) -> int:
    field = [[c for c in row] for row in data.splitlines()]
    seen_tiles = run_ray((0, 0), field, 3)
    energized_tiles = set([(t[0], t[1]) for t in seen_tiles])
    return len(energized_tiles)


def question_2(data: str) -> int:
    field = [[c for c in row] for row in data.splitlines()]
    max_energy = 0
    for c in range(len(field[0])):
        seen_tiles = run_ray((0, c), field, 2)
        energized_tiles = set([(t[0], t[1]) for t in seen_tiles])
        max_energy = max(len(energized_tiles), max_energy)
        seen_tiles = run_ray((len(field) - 1, c), field, 0)
        energized_tiles = set([(t[0], t[1]) for t in seen_tiles])
        max_energy = max(len(energized_tiles), max_energy)
    for r in range(len(field)):
        seen_tiles = run_ray((r, 0), field, 3)
        energized_tiles = set([(t[0], t[1]) for t in seen_tiles])
        max_energy = max(len(energized_tiles), max_energy)
        seen_tiles = run_ray((r, len(field[0]) - 1), field, 0)
        energized_tiles = set([(t[0], t[1]) for t in seen_tiles])
        max_energy = max(len(energized_tiles), max_energy)
    return max_energy


def test_question_1():
    data = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""
    res = question_1(data)
    assert res == 46


def test_question_2():
    data = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""
    res = question_2(data)
    assert res == 51


if __name__ == "__main__":
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
