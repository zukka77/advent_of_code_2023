from pathlib import Path
import heapq

BASE_DIR = Path(__file__).parent

# 0=up 1=left 2=down 3=right
DR = [-1, 0, 1, 0]  # row movement on direction
DC = [0, -1, 0, 1]  # column movement on direction


def find_path(city: list[list[int]], start: tuple[int, int]) -> int:
    r, c = start
    # contains the tiles to visit oredered by increasing distance
    to_visit = [[0, r, c, 3, 1]]
    n_rows = len(city)
    n_cols = len(city[0])
    seen = {}
    while to_visit:
        # pop the nearest tiles to try
        distance, r, c, direction, n_direction = heapq.heappop(to_visit)
        if (r, c, direction, n_direction) in seen:
            continue
        if n_direction <= 3:
            seen[(r, c, direction, n_direction)] = distance
            for d in [-1, 0, 1]:
                # go in every direction except backward
                new_direction = (direction + d) % 4
                if (
                    r + DR[new_direction] >= 0
                    and r + DR[new_direction] < n_rows
                    and c + DC[new_direction] >= 0
                    and c + DC[new_direction] < n_cols
                ):
                    heapq.heappush(
                        to_visit,
                        [
                            distance + city[r + DR[new_direction]][c + DC[new_direction]],
                            r + DR[new_direction],
                            c + DC[new_direction],
                            new_direction,
                            (n_direction + 1) if direction == new_direction else 1,
                        ],
                    )
    return min([seen[(r, c, dir, n_dir)] for r, c, dir, n_dir in seen if r == n_rows - 1 and c == n_cols - 1])


def find_path2(city: list[list[int]], start: tuple[int, int]) -> int:
    r, c = start
    # contains the tiles to visit oredered by increasing distance
    to_visit = [[0, r, c, 3, 1]]
    n_rows = len(city)
    n_cols = len(city[0])
    seen = {}
    while to_visit:
        # pop the nearest tiles to try
        distance, r, c, direction, n_direction = heapq.heappop(to_visit)
        if (r, c, direction, n_direction) in seen:
            continue
        if n_direction <= 10:
            if n_direction >= 4:
                seen[(r, c, direction, n_direction)] = distance
            for d in [-1, 0, 1] if n_direction >= 4 else [0]:
                # go in every direction except backward unless we made less than 4 steps in which case we have to go straight
                new_direction = (direction + d) % 4
                if (
                    r + DR[new_direction] >= 0
                    and r + DR[new_direction] < n_rows
                    and c + DC[new_direction] >= 0
                    and c + DC[new_direction] < n_cols
                ):
                    heapq.heappush(
                        to_visit,
                        [
                            distance + city[r + DR[new_direction]][c + DC[new_direction]],
                            r + DR[new_direction],
                            c + DC[new_direction],
                            new_direction,
                            (n_direction + 1) if direction == new_direction else 1,
                        ],
                    )
    return min(
        [
            seen[(r, c, direction, n_direction)]
            for r, c, direction, n_direction in seen
            if r == n_rows - 1 and c == n_cols - 1
        ]
    )


def question_1(data: str) -> int:
    city = [[int(v) for v in row] for row in data.splitlines()]
    heat_loss = find_path(city, (0, 0))
    return heat_loss


def question_2(data: str) -> int:
    city = [[int(v) for v in row] for row in data.splitlines()]
    heat_loss = find_path2(city, (0, 0))
    return heat_loss


def test_question_1():
    data = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
    res = question_1(data)
    assert res == 102


def test_question_2():
    data = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
    res = question_2(data)
    assert res == 94
    data = """111111111111
999999999991
999999999991
999999999991
999999999991"""
    res = question_2(data)
    assert res == 71


if __name__ == "__main__":
    test_question_1()
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
