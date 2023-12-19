from pathlib import Path

BASE_DIR = Path(__file__).parent

# https://www.youtube.com/watch?v=bGWK76_e-LM
# https://en.wikipedia.org/wiki/Shoelace_formula
# https://en.wikipedia.org/wiki/Pick%27s_theorem


def find_area(commands: list[tuple[str, int, int]]) -> int:
    dir = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    pos = (0, 0)
    points = [pos]
    n_points = 0
    for direction, steps, _ in commands:
        n_points += steps
        new_pos = (pos[0] + dir[direction][0] * steps, pos[1] + dir[direction][1] * steps)
        points.append(new_pos)
        pos = new_pos
    # shoelace formula to calculate the area
    area = (
        abs(sum([points[i][1] * (points[(i + 1) % len(points)][0] - points[i - 1][0]) for i in range(len(points))]))
        // 2
    )
    # internal point (based on Pick's theorem)
    i = area - n_points // 2 + 1

    # area is equal to number of internal points + n of edge points
    return i + n_points


def question_1(data: str) -> int:
    commands = []
    for row in data.splitlines():
        direction, steps, color = row.split()
        commands.append((direction, int(steps), color[2:-1]))
    return find_area(commands)


def question_2(data: str) -> int:
    commands = []
    # translate new instructions to old
    dirs = {"0": "R", "1": "D", "2": "L", "3": "U"}
    for row in data.splitlines():
        _, _, instruction = row.split()
        commands.append((dirs[instruction[-2]], int(instruction[2:7], 16), None))
    return find_area(commands)


def test_question_1():
    data = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""
    res = question_1(data)
    assert res == 62


def test_question_2():
    data = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""
    res = question_2(data)
    assert res == 952408144115


if __name__ == "__main__":
    test_question_1()
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
