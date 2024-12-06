from typing import Iterator, List, Dict, Tuple
import itertools
import functools
import sys


def str_to_rule(s: str) -> Tuple[int, int]:
    l = s.strip().split("|")
    return (int(l[0]), int(l[1]))


def build_db(db: Dict[int, List[int]], rule: Tuple[int, int]) -> Dict[int, List[int]]:
    if rule[0] in db:
        db[rule[0]].append(rule[1])
    else:
        db[rule[0]] = [rule[1]]

    return db


def load_rules(source: Iterator[str]) -> Dict[int, List[int]]:
    rule_str_source = itertools.takewhile(lambda s: len(s) > 1, source)
    rule_int_source = map(str_to_rule, rule_str_source)
    return functools.reduce(build_db, rule_int_source, {})
    # return list(map(str_to_rule, rule_str_source))


def load_changes(source: Iterator[str]) -> List[List[int]]:
    return list(map(lambda s: [int(i) for i in s.strip().split(",")], source))


def change_breaks_rules(change: List[int], rules: Dict[int, List[int]]) -> bool:
    # print(f"{change=}")
    rule_broken = False
    for index, item in enumerate(change):
        pre_items = change[:index]
        # print(f"{item=}")
        for proceeding_item in rules.get(item, []):
            # print(f"checking {proceeding_item}")
            if proceeding_item in pre_items:
                # print(f"  found {proceeding_item} before")
                return True
    return rule_broken


def get_middle_item(change: List[int]) -> int:
    change_len = len(change)
    if change_len % 2 == 0:
        raise ValueError("Cant have a middle of an even lengthed set of numbers")
    return change[int((change_len - 1) / 2)]


def shuffle_change(change: List[int], rules: Dict[int, List[int]]) -> List[int]:
    while True:
        change_made = False
        # find problematic entry
        for i in range(len(change)):
            v = change[i]
            for rule_entry in rules.get(v, []):
                # if rule entry exists before the intended number
                if rule_entry in change[:i]:
                    change.remove(rule_entry)
                    change.insert(i, rule_entry)
                    change_made = True

        if not change_made:
            break

    return change


def main():
    stdin = sys.stdin
    rules = load_rules(stdin)
    changes = load_changes(stdin)
    sum = 0
    for change in changes:
        if change_breaks_rules(change, rules):
            change = shuffle_change(change, rules)
            assert not change_breaks_rules(change, rules)
            sum += get_middle_item(change)

    print(f"{sum=}")


if __name__ == "__main__":
    main()


def test_load_rules():
    rules = None
    with open("days/05/jamie/data/test_data.txt") as fp:
        rules = load_rules(fp)
    assert sum(len(values) for k, values in rules.items()) == 21


def test_load_changes():
    rules = None
    with open("days/05/jamie/data/test_data.txt") as fp:
        rules = load_rules(fp)
        changes = load_changes(fp)

    assert len(changes) == 6
    assert changes[-1] == [97, 13, 75, 29, 47]


def test_change_breaks_rules():
    rules = None
    with open("days/05/jamie/data/test_data.txt") as fp:
        rules = load_rules(fp)

    assert not change_breaks_rules([75, 47, 61, 53, 29], rules)
    assert not change_breaks_rules([97, 61, 53, 29, 13], rules)
    assert not change_breaks_rules([75, 29, 13], rules)
    assert change_breaks_rules([75, 97, 47, 61, 53], rules)
    assert change_breaks_rules([61, 13, 29], rules)
    assert change_breaks_rules([97, 13, 75, 29, 47], rules)


def test_shuffle_change():
    rules = None
    with open("days/05/jamie/data/test_data.txt") as fp:
        rules = load_rules(fp)

    assert shuffle_change([75, 97, 47, 61, 53], rules) == [97, 75, 47, 61, 53]
    assert shuffle_change([61, 13, 29], rules) == [61, 29, 13]
    assert shuffle_change([97, 13, 75, 29, 47], rules) == [97, 75, 47, 29, 13]
