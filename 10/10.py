from pathlib import Path


BASE_DIR = Path(__file__).parent


def get_valid_steps(start: tuple[int, int], g: list[list[str]]) -> list[tuple[int, int]]:
    nrows = len(g)
    ncols = len(g[0])
    good_steps = []
    for r in range(max(start[0] - 1, 0), min(nrows, start[0] + 2)):
        if r < start[0]:
            # UP
            if g[start[0]][start[1]] in ("|", "S", "L", "J") and g[r][start[1]] in ("|", "F", "7", "S"):
                good_steps.append((r, start[1]))
        elif r > start[0]:
            # DOWN
            if g[start[0]][start[1]] in ("|", "S", "7", "F") and g[r][start[1]] in ("|", "J", "L", "S"):
                good_steps.append((r, start[1]))

    for c in range(max(0, start[1] - 1), min(ncols, start[1] + 2)):
        if c < start[1]:
            # LEFT
            if g[start[0]][start[1]] in ("-", "S", "7", "J") and g[start[0]][c] in ("-", "L", "F", "S"):
                good_steps.append((start[0], c))
        if c > start[1]:
            # RIGHT
            if g[start[0]][start[1]] in ("-", "S", "L", "F") and g[start[0]][c] in ("-", "7", "J", "S"):
                good_steps.append((start[0], c))
    return sorted(good_steps)


def find_loop(start: tuple[int, int], g: list[list[str]]) -> list[tuple[int, int]]:
    path = [start]
    next_steps = get_valid_steps(start, g)
    del next_steps[1]
    while next_steps:
        for step in next_steps:
            next_steps.remove(step)
            if step in path:
                continue
            path.append(step)
            next_steps += get_valid_steps(step, g)

    return path


def question_1(data: str) -> int:
    g = [[c for c in row] for row in data.splitlines()]
    # find starting point
    start = None
    for r, row in enumerate(g):
        for c, val in enumerate(row):
            if val == "S":
                start = (r, c)
                break
        if start:
            break
    assert start is not None
    path = find_loop(start, g)
    return len(path) // 2


def question_2(data: str) -> int:
    g = [[c for c in row] for row in data.splitlines()]
    # find starting point
    start = None
    for r, row in enumerate(g):
        for c, val in enumerate(row):
            if val == "S":
                start = (r, c)
                break
        if start:
            break
    assert start is not None
    path = set(find_loop(start, g))
    n_dots = 0
    for r, row in enumerate(g):
        inside = False
        ncandidates = 0
        for c, val in enumerate(row):
            if (r, c) not in path:
                if inside:
                    ncandidates += 1
                continue
            if (r, c) in path and val in ("|", "L", "J", "S"):
                if inside:
                    n_dots += ncandidates
                ncandidates = 0
                inside = not inside
    return n_dots


def test_question_1():
    data = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""
    res = question_1(data)
    assert res == 4
    data = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""
    res = question_1(data)
    assert res == 8


def test_question_2():
    data = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""
    res = question_2(data)
    assert res == 4
    data = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""
    res = question_2(data)
    assert res == 8
    data = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""
    res = question_2(data)
    assert res == 10


if __name__ == "__main__":
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
