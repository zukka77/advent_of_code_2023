from pathlib import Path

BASE_DIR = Path(__file__).parent


def question_1(data: str) -> int:
    sum = 0
    for line in data.splitlines():
        numbers = list(filter(lambda x: x.isdigit(), line))
        sum += int(numbers[0] + numbers[-1])

    return sum


def question_2(data: str) -> int:
    digits = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    sum = 0
    for line in data.splitlines():
        digit1 = ""
        digit2 = ""
        for i in range(len(line)):
            for digit in digits:
                if line[i:].startswith(digit):
                    digit1 = digits[digit]
                    break
            if digit1:
                break
        for i in range(len(line) - 1, -1, -1):
            for digit in digits:
                if line[i:].startswith(digit):
                    digit2 = digits[digit]
                    break
            if digit2:
                break
        sum += int(digit1 + digit2)
    return sum


def test_question_1():
    data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    res = question_1(data)
    assert res == 142


def test_question_2():
    data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    res = question_2(data)
    assert res == 281


if __name__ == "__main__":
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
