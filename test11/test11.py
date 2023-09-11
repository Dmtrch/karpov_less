from typing import List, Tuple



def extend_matches(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    matches = set(pairs)
    items = set()
    for pair in pairs:
        item1, item2 = pair
        items.add(item1)
        items.add(item2)

    for i1 in items:
        for i2 in items:
            if i1 < i2 and (i1, i2) not in matches:
                if any(i1 in pair and i2 in pair for pair in matches):
                    matches.add((i1, i2))

    return sorted(list(matches))

a = extend_matches([(1, 2), (2, 3), (3, 4)])

print(a)