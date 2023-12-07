from pathlib import Path


BASE_DIR = Path(__file__).parent


def question_1(data: str) -> int:
    lines = data.splitlines()
    times = map(int, lines[0].split(":")[1].split())
    distances = map(int, lines[1].split(":")[1].split())
    races = list(zip(times, distances))
    res = 1
    for race in races:
        time, distance = race
        low = 0
        high = time // 2
        guess = 0
        # print(f"{race}")
        while low <= high:
            guess = (high + low) // 2
            if guess * (time - guess) <= distance:
                low = guess + 1
            elif guess * (time - guess) > distance:
                high = guess - 1
                last_high = guess
            else:
                break

        # print(f"{race}:{guess} {time - 2*guess +1}")
        res *= time - 2 * (last_high) + 1
    return res


def question_2(data: str) -> int:
    lines = data.splitlines()
    time = int("".join(lines[0].split(":")[1].split()))
    distance = int("".join(lines[1].split(":")[1].split()))
    print("time: {time} distance: {distance}")
    low = 0
    high = time // 2
    guess = 0
    # print(f"{race}")
    while low <= high:
        guess = (high + low) // 2
        if guess * (time - guess) <= distance:
            low = guess + 1
        elif guess * (time - guess) > distance:
            high = guess - 1
            last_high = guess
        else:
            break

    # print(f"{race}:{guess} {time - 2*guess +1}")
    res = time - 2 * (last_high) + 1
    return res


def test_question_1():
    data = """Time:      7  15   30
Distance:  9  40  200"""
    res = question_1(data)
    assert res == 288


def test_question_2():
    data = """Time:      7  15   30
Distance:  9  40  200"""
    res = question_2(data)
    assert res == 71503


if __name__ == "__main__":
    test_question_1()
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
