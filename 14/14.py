from pathlib import Path
from copy import deepcopy

BASE_DIR = Path(__file__).parent


def roll(field: list[list[str]], direction: int = 0) -> list[list[str]]:
    """rolls the field d in [0,1,2,3] -> [N,W,S,E] Modifies field!"""
    if direction in [0, 1]:
        for c in range(len(field)):
            for r in range(len(field[0])):
                if field[r][c] == "O":
                    if direction == 0:
                        rr = r
                        while rr - 1 >= 0 and field[rr - 1][c] == ".":
                            rr -= 1
                        if rr != r:
                            field[r][c] = "."
                            field[rr][c] = "O"
                    elif direction == 1:
                        cc = c
                        while cc - 1 >= 0 and field[r][cc - 1] == ".":
                            cc -= 1
                        if cc != c:
                            field[r][c] = "."
                            field[r][cc] = "O"
    elif direction in [2, 3]:
        for c in range(len(field) - 1, -1, -1):
            for r in range(len(field[0]) - 1, -1, -1):
                if field[r][c] == "O":
                    if direction == 2:
                        rr = r
                        while rr + 1 < len(field) and field[rr + 1][c] == ".":
                            rr += 1
                        if rr != r:
                            field[r][c] = "."
                            field[rr][c] = "O"
                    elif direction == 3:
                        cc = c
                        while cc + 1 < len(field[0]) and field[r][cc + 1] == ".":
                            cc += 1
                        if cc != c:
                            field[r][c] = "."
                            field[r][cc] = "O"
    else:
        assert False, f"invalid direction: {direction}"
    return field


def get_load(field: list[list[str]]) -> int:
    load = 0
    for r, row in enumerate(field):
        load += len(list(filter(lambda x: x == "O", row))) * (len(field) - r)
    return load


def question_1(data: str) -> int:
    field = [[v for v in row] for row in data.splitlines()]
    roll(field)
    return get_load(field)


def question_2(data: str) -> int:
    field = [[v for v in row] for row in data.splitlines()]
    old_field = deepcopy(field)
    history = [old_field]
    for _ in range(1000000000):
        for d in [0, 1, 2, 3]:
            field = roll(field, d)
        if field in history:
            break
        old_field = deepcopy(field)
        history.append(old_field)
    for i in range((1000000000 - history.index(field)) % (len(history) - history.index(field))):
        for d in [0, 1, 2, 3]:
            field = roll(field, d)
    return get_load(field)


def test_rolling():
    data = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
    res = None
    field = [[v for v in row] for row in data.splitlines()]
    print("\n".join([" ".join(row) for row in field]))
    print("-" * 80)
    for d in [0, 1, 2, 3]:
        res = roll(field, d)
        print("\n".join([" ".join(row) for row in field]))
        print("-" * 80)
    assert (
        "\n".join(["".join(row) for row in res])
        == """.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#...."""
    )
    for d in [0, 1, 2, 3]:
        res = roll(field, d)
    assert (
        "\n".join(["".join(row) for row in res])
        == """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O"""
    )
    for d in [0, 1, 2, 3]:
        res = roll(field, d)
    assert (
        "\n".join(["".join(row) for row in res])
        == """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O"""
    )


def test_question_1():
    data = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
    res = question_1(data)
    assert res == 136


def test_question_2():
    data = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
    res = question_2(data)
    assert res == 64


if __name__ == "__main__":
    test_question_2()
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
