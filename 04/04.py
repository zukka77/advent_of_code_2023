from pathlib import Path
from functools import reduce

BASE_DIR = Path(__file__).parent


def question_1(data: str) -> int:
    sum = 0
    for line in data.splitlines():
        game, numbers = line.split(":")
        winning_numbers, play_numbers = numbers.split("|")
        winning_numbers = set([int(x) for x in winning_numbers.split()])
        play_numbers = set([int(x) for x in play_numbers.split()])
        n_ok = len(play_numbers.intersection(winning_numbers))
        if n_ok:
            sum += 2 ** (n_ok - 1)
    return sum


def question_2(data: str) -> int:
    cards = dict()
    for line in data.splitlines():
        game, numbers = line.split(":")
        card_number = int(game.split()[1])
        winning_numbers, play_numbers = numbers.split("|")

        winning_numbers = set([int(x) for x in winning_numbers.split()])
        play_numbers = set([int(x) for x in play_numbers.split()])
        n_ok = len(play_numbers.intersection(winning_numbers))

        if card_number not in cards:
            cards[card_number] = 1
        cardinality = cards[card_number]

        for n in range(n_ok):
            cards[card_number + n + 1] = cards.get(card_number + n + 1, 1) + cardinality

    return reduce(lambda a, b: a + b, cards.values(), 0)


def test_question_1():
    data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    res = question_1(data)
    assert res == 13


def test_question_2():
    data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    res = question_2(data)
    assert res == 30


if __name__ == "__main__":
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
