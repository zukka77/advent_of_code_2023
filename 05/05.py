from pathlib import Path
from collections import namedtuple

BASE_DIR = Path(__file__).parent

tabline = namedtuple("tabline", ["target", "start", "length"])


def get_overlap(a: list[int], b: list[int]) -> int:
    return max(0, min(a[1], b[1]) - max(a[0], b[0]))


def question_1(data: str) -> int:
    lines = data.splitlines()
    seeds = list(map(int, lines[0].split(":")[1].split()))
    tables = []
    cur_table = []

    for line in lines[3:]:
        if not line:
            if cur_table:
                tables.append(cur_table)
                cur_table = []
            continue
        if line.endswith(":"):
            continue
        target, start, length = list(map(int, line.split()))
        cur_table.append(tabline(target, start, length))
    min_loc = tables[-1][-1].start

    for loc in seeds:
        for table in tables:
            for entry in table:
                if loc >= entry.start and loc < entry.start + entry.length:
                    loc += entry.target - entry.start
                    break
        min_loc = min(min_loc, loc)
    return min_loc


def question_2(data: str) -> int:
    lines = data.splitlines()
    seeds = list(map(int, lines[0].split(":")[1].split()))
    tables = []
    cur_table = []

    for line in lines[3:]:
        if not line:
            if cur_table:
                tables.append(cur_table)
                cur_table = []
            continue
        if line.endswith(":"):
            continue
        target, start, length = list(map(int, line.split()))
        cur_table.append(tabline(target, start, length))
    min_loc = tables[-1][-1].start
    import pprint

    # for i in range(0, len(seeds), 2):
    #    for loc in range(seeds[i], seeds[i] + seeds[i + 1]):
    #        for table in tables:
    #            for entry in table:
    #                if loc >= entry.start and loc < entry.start + entry.length:
    #                    loc += entry.target - entry.start
    #                    break
    #        min_loc = min(min_loc, loc)
    start_ranges = []
    for i in range(0, len(seeds), 2):
        start_ranges.append(tabline(seeds[i], seeds[i], seeds[i + 1]))

    tables.insert(0, start_ranges)
    pprint.pprint(tables)
    for i, table in enumerate(tables):
        for r in table:
            ...
    return


def test_question_1():
    data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4

"""
    res = question_1(data)
    assert res == 35


def test_question_2():
    data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4

"""
    res = question_2(data)
    assert res == 46


if __name__ == "__main__":
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    # res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    # print(f"Question 2: {res}")
    test_question_2()
