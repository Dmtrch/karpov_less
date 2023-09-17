from typing import List


def extend_matches(groups: List[tuple]) -> List[tuple]:
    list_sets = [set(group) for group in groups]

    len_set = len(list_sets)
    first_set = 0
    # проходим по всем группам
    while first_set < len_set:

        second_set = 0

        while second_set < len_set:
            if list_sets[first_set] & list_sets[second_set] and first_set != second_set:  # если есть общие числа

                list_sets[first_set] = list_sets[first_set]|list_sets[second_set]
                list_sets.remove(list_sets[second_set])
                len_set -= 1

            second_set += 1

        first_set += 1

    groups = [tuple(s) for s in list_sets if s]
    groups = [sorted(s) for s in groups]
    groups = [tuple(s) for s in groups]
    def sorting_key(some_tuple):
        return some_tuple

    groups = sorted(groups, key=sorting_key)

    return groups

a = extend_matches([(5, 3, 4, 8), (1, 2), (7, 2)])
# [(1, 2, 7), (3, 4, 5, 8)]
print(a)