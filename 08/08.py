from pathlib import Path
import re
from math import lcm

BASE_DIR = Path(__file__).parent


def question_1(data: str) -> int:
    lines = data.splitlines()
    lr_sequence = lines[0]
    G = {}
    line_pattern = re.compile(r"\w+")
    for line in lines[2:]:
        node, *nodes = line_pattern.findall(line)
        G[node] = tuple(nodes)
    # print(G)
    i = 0
    curr_node = "AAA"
    # print(f"curr_node: {curr_node}")
    while curr_node != "ZZZ":
        # print(G[curr_node][0 if lr_sequence[i % len(lr_sequence)] == "L" else 1])
        curr_node = G[curr_node][0 if lr_sequence[i % len(lr_sequence)] == "L" else 1]
        i += 1
    return i


def question_2a(data: str) -> int:
    lines = data.splitlines()
    lr_sequence = lines[0]
    G = {}
    line_pattern = re.compile(r"\w+")
    for line in lines[2:]:
        node, *nodes = line_pattern.findall(line)
        G[node] = tuple(nodes)
    # print(G)

    current_nodes = list(filter(lambda x: x.endswith("A"), G.keys()))
    print(list(current_nodes))
    i = 0
    while list(filter(lambda x: not x.endswith("Z"), current_nodes)):
        for n, node in enumerate(current_nodes):
            current_nodes[n] = G[node][0 if lr_sequence[i % len(lr_sequence)] == "L" else 1]
        i += 1
    return i


def question_2(data: str) -> int:
    lines = data.splitlines()
    lr_sequence = lines[0]
    G = {}
    line_pattern = re.compile(r"\w+")
    for line in lines[2:]:
        node, *nodes = line_pattern.findall(line)
        G[node] = tuple(nodes)
    # print(G)

    current_nodes = list(filter(lambda x: x.endswith("A"), G.keys()))
    print(list(current_nodes))
    periods: list[int] = []
    for node in current_nodes:
        i = 0
        while not node.endswith("Z"):
            node = G[node][0 if lr_sequence[i % len(lr_sequence)] == "L" else 1]
            i += 1
        periods.append(i)

    return lcm(*periods)


def test_question_1():
    data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""
    res = question_1(data)
    assert res == 2
    data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
    res = question_1(data)
    assert res == 6


def test_question_2():
    data = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
    res = question_2(data)
    assert res == 6


if __name__ == "__main__":
    res = question_1(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 1: {res}")
    res = question_2(Path(BASE_DIR / "INPUT").read_text(encoding="utf8"))
    print(f"Question 2: {res}")
