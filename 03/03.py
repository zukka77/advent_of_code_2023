from pathlib import Path


BASE_DIR = Path(__file__).parent


def get_overlap(a: list[int], b: list[int]) -> int:
    return max(0, min(a[1], b[1]) - max(a[0], b[0]) + 1)


def question_1(data: str) -> int:
    sum = 0
    numbers: dict[int, list[dict[str, int]]] = {}
    schematic = data.splitlines()
    for i, line in enumerate(schematic):
        digits = []
        for j, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            else:
                if digits:
                    numbers[i] = numbers.get(i, []) + [
                        {"n": int("".join(digits)), "rmin": j - len(digits), "rmax": j - 1}
                    ]
                    digits = []
        if digits:
            numbers[i] = numbers.get(i, []) + [
                {"n": int("".join(digits)), "rmin": len(line) - len(digits), "rmax": len(line) - 1}
            ]

    for i in range(len(schematic)):
        for j in range(len(schematic[0])):
            c = schematic[i][j]
            if not c.isdigit() and c != ".":
                # up
                if i > 0 and i - 1 in numbers:
                    values = list(
                        filter(
                            lambda x: get_overlap(
                                [max(0, j - 1), min(len(schematic[i]), j + 1)], [x["rmin"], x["rmax"]]
                            )
                            > 0,
                            numbers[i - 1],
                        )
                    )
                    for value in values:
                        sum += value["n"]
                        numbers[i - 1].remove(value)
                # left
                if j > 0 and i in numbers:
                    values = list(filter(lambda x: j - 1 >= x["rmin"] and j - 1 <= x["rmax"], numbers[i]))
                    for value in values:
                        sum += value["n"]
                        numbers[i].remove(value)
                # right
                if j < len(schematic[i]) - 1 and i in numbers:
                    values = list(filter(lambda x: j + 1 >= x["rmin"] and j + 1 <= x["rmax"], numbers[i]))
                    for value in values:
                        sum += value["n"]
                        numbers[i].remove(value)
                # down
                if i < len(schematic) - 1 and i - 1 in numbers:
                    values = list(
                        filter(
                            lambda x: get_overlap(
                                [max(0, j - 1), min(len(schematic[i]), j + 1)], [x["rmin"], x["rmax"]]
                            )
                            > 0,
                            numbers[i + 1],
                        )
                    )
                    for value in values:
                        sum += value["n"]
                        numbers[i + 1].remove(value)
    return sum


def question_2(data: str) -> int:
    sum = 0
    numbers: dict[int, list[dict[str, int]]] = {}
    schematic = data.splitlines()
    for i, line in enumerate(schematic):
        digits = []
        for j, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            else:
                if digits:
                    numbers[i] = numbers.get(i, []) + [
                        {"n": int("".join(digits)), "rmin": j - len(digits), "rmax": j - 1}
                    ]
                    digits = []
        if digits:
            numbers[i] = numbers.get(i, []) + [
                {"n": int("".join(digits)), "rmin": len(line) - len(digits), "rmax": len(line) - 1}
            ]

    for i in range(len(schematic)):
        for j in range(len(schematic[0])):
            c = schematic[i][j]
            if c == "*":
                gears = []
                # up
                if i > 0 and i - 1 in numbers:
                    values = list(
                        filter(
                            lambda x: get_overlap(
                                [max(0, j - 1), min(len(schematic[i]), j + 1)], [x["rmin"], x["rmax"]]
                            )
                            > 0,
                            numbers[i - 1],
                        )
                    )
                    for value in values:
                        gears.append(value)
                        numbers[i - 1].remove(value)
                # left
                if j > 0 and i in numbers:
                    values = list(filter(lambda x: j - 1 >= x["rmin"] and j - 1 <= x["rmax"], numbers[i]))
                    for value in values:
                        gears.append(value)
                        numbers[i].remove(value)
                # right
                if j < len(schematic[i]) - 1 and i in numbers:
                    values = list(filter(lambda x: j + 1 >= x["rmin"] and j + 1 <= x["rmax"], numbers[i]))
                    for value in values:
                        gears.append(value)
                        numbers[i].remove(value)
                # down
                if i < len(schematic) - 1 and i - 1 in numbers:
                    values = list(
                        filter(
                            lambda x: get_overlap(
                                [max(0, j - 1), min(len(schematic[i]), j + 1)], [x["rmin"], x["rmax"]]
                            )
                            > 0,
                            numbers[i + 1],
                        )
                    )
                    for value in values:
                        gears.append(value)
                        numbers[i + 1].remove(value)
                if len(gears) == 2:
                    sum += gears[0]["n"] * gears[1]["n"]
    return sum


def test_question_1():
    data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    res = question_1(data)
    assert res == 4361


def test_question_2():
    data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    res = question_2(data)
    assert res == 467835


if __name__ == "__main__":
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
