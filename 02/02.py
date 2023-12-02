from pathlib import Path

BASE_DIR = Path(__file__).parent


def question_1(data: str) -> int:
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    sum = 0
    for line in data.splitlines():
        line_split = line.split(":")
        game_id = int(line_split[0].split(" ")[1])
        all_ok = True
        for hand in line_split[1].split(";"):
            for cube in hand.split(","):
                cube = cube.strip()
                (n, color) = cube.split(" ")
                n = int(n)
                if n > max_cubes[color]:
                    all_ok = False
                    break
        if all_ok:
            sum += game_id
    return sum


def question_2(data: str) -> int:
    sum = 0
    for line in data.splitlines():
        line_split = line.split(":")
        max_colors = {}
        for hand in line_split[1].split(";"):
            for cube in hand.split(","):
                cube = cube.strip()
                (n, color) = cube.split(" ")
                n = int(n)
                max_colors[color] = max(max_colors.get(color, 0), n)
        cpow = 1
        for c in max_colors.values():
            cpow *= c
        sum += cpow
    return sum


def test_question_1():
    data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    res = question_1(data)
    assert res == 8


def test_question_2():
    data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    res = question_2(data)
    assert res == 2286


if __name__ == "__main__":
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
