from pathlib import Path

BASE_DIR = Path(__file__).parent


def get_hand_value(hand: str) -> int:
    cards = {}
    for card in hand:
        cards[card] = cards.get(card, 0) + 1
    distinct_type = len(cards.keys())
    if distinct_type == 5:
        return 1
    if distinct_type == 1:
        return 7
    if distinct_type == 2:
        if 4 in cards.values():
            return 6
        if 3 in cards.values():
            return 5
    if distinct_type == 3:
        if 3 in cards.values():
            return 4
        if 2 in cards.values():
            return 3
    return 2


def get_hand_value_joker(hand: str) -> int:
    cards = {}
    for card in hand:
        cards[card] = cards.get(card, 0) + 1
    n_joker = cards.get("J", 0)
    if n_joker and n_joker != 5:
        del cards["J"]
        max_value = 0
        card_type = None
        for card, value in cards.items():
            if value > max_value or (
                value == max_value
                and card.replace("A", "D").replace("K", "C").replace("Q", "B").replace("J", "1").replace("T", "A")
                > card_type.replace("A", "D").replace("K", "C").replace("Q", "B").replace("J", "1").replace("T", "A")
            ):
                max_value = value
                card_type = card

        cards[card_type] += n_joker

    distinct_type = len(cards.keys())
    if distinct_type == 5:
        return 1
    if distinct_type == 1:
        return 7
    if distinct_type == 2:
        if 4 in cards.values():
            return 6
        if 3 in cards.values():
            return 5
    if distinct_type == 3:
        if 3 in cards.values():
            return 4
        if 2 in cards.values():
            return 3
    return 2


def compare_hands_key(hand: dict) -> str:
    return str(hand["value"]) + hand["hand"].replace("A", "E").replace("K", "D").replace("Q", "C").replace(
        "J", "B"
    ).replace("T", "A")


def compare_hands_key_joker(hand: dict) -> str:
    return str(hand["value"]) + hand["hand"].replace("A", "D").replace("K", "C").replace("Q", "B").replace(
        "J", "1"
    ).replace("T", "A")


def question_1(data: str) -> int:
    hands = []
    for line in data.splitlines():
        hand, bid = line.split()
        bid = int(bid)
        value = get_hand_value(hand)
        hands.append({"hand": hand, "bid": bid, "value": value})
    hands.sort(key=compare_hands_key)
    res = 0
    for i, hand in enumerate(hands):
        res += (i + 1) * hand["bid"]
    return res


def question_2(data: str) -> int:
    hands = []
    for line in data.splitlines():
        hand, bid = line.split()
        bid = int(bid)
        value = get_hand_value_joker(hand)
        hands.append({"hand": hand, "bid": bid, "value": value})
    hands.sort(key=compare_hands_key_joker)
    res = 0
    for i, hand in enumerate(hands):
        # print(f"{i} {hand}")
        res += (i + 1) * hand["bid"]
    return res


def test_question_1():
    data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    res = question_1(data)
    assert res == 6440


def test_question_2():
    data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    res = question_2(data)
    assert res == 5905


if __name__ == "__main__":
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
