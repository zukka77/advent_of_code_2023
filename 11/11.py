from pathlib import Path

BASE_DIR = Path(__file__).parent


def expand_universe(universe: list[list[str]]) -> list[list[str]]:
    new_universe: list[list[str]] = []
    cols = [[r[c] for r in universe] for c in range(len(universe[0]))]
    exp_cols = []
    for c, col in enumerate(cols):
        if all([x == "." for x in col]):
            exp_cols.append(c + len(exp_cols))
    for c in exp_cols:
        for row in universe:
            row.insert(c, ".")
    for row in universe:
        new_universe.append(row)
        if all([x == "." for x in row]):
            new_universe.append([*row])
    return new_universe


def universe_expand_factor(universe: list[list[str]], expansion_factor=1) -> tuple[list[int], list[int]]:
    new_universe: list[list[str]] = []
    cols = [[r[c] for r in universe] for c in range(len(universe[0]))]
    exp_cols = []
    for c, col in enumerate(cols):
        if all([x == "." for x in col]):
            # exp_cols.append(c + len(exp_cols) * expansion_factor)
            exp_cols.append(c)
    exp_rows = []
    for r, row in enumerate(universe):
        new_universe.append(row)
        if all([x == "." for x in row]):
            # exp_rows.append(r + len(exp_rows) * expansion_factor)
            exp_rows.append(r)
    return (exp_rows, exp_cols)


def distance(start: tuple[int, int], end: tuple[int, int]) -> int:
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def question_1(data: str) -> int:
    universe = [[c for c in line] for line in data.splitlines()]
    universe = expand_universe(universe)
    galaxies = []
    for r, row in enumerate(universe):
        for c, val in enumerate(row):
            if val == "#":
                galaxies.append((r, c))
    galaxy_pairs = [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1 :]]
    res = 0
    for pair in galaxy_pairs:
        res += distance(*pair)
    return res


def question_2(data: str, expansion_factor=1_000_000) -> int:
    universe = [[c for c in line] for line in data.splitlines()]
    rows_expansion, cols_expansion = universe_expand_factor(universe, expansion_factor)
    galaxies = []
    for r, row in enumerate(universe):
        for c, val in enumerate(row):
            if val == "#":
                galaxies.append((r, c))
    # inflate galaxies
    for i, galaxy in enumerate(galaxies):
        expanded_rows = len(list(filter(lambda x: x < galaxy[0], rows_expansion)))
        expanded_cols = len(list(filter(lambda x: x < galaxy[1], cols_expansion)))
        galaxies[i] = (
            galaxy[0] - expanded_rows + expansion_factor * expanded_rows,
            galaxy[1] - expanded_cols + expansion_factor * expanded_cols,
        )
    galaxy_pairs = [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1 :]]
    res = 0
    for pair in galaxy_pairs:
        res += distance(*pair)
    return res


def test_expand_universe():
    data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
    expected_res = """....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""
    res = expand_universe([[x for x in line] for line in data.splitlines()])
    res = "\n".join(["".join(line) for line in res])
    assert res == expected_res


def test_question_1():
    data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
    res = question_1(data)
    assert res == 374


def test_question_2():
    data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
    res = question_2(data, 2)
    assert res == 374
    res = question_2(data, 10)
    assert res == 1030
    res = question_2(data, 100)
    assert res == 8410


if __name__ == "__main__":
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
