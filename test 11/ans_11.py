from typing import List
from typing import Tuple

def extend_matches(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    list_sets = list()

    for pair in pairs:
        new_set = set(pair)
        list_sets.append(new_set)

    result = list_sets

# проходим по всем парам
    for first_set in range(len(list_sets)):
        for second_set in range(len(list_sets[first_set+1:])):
            if list_sets[first_set] & list_sets[second_set]:#если есть общие числа
                new_set = list_sets[first_set].symmetric_difference(list_sets[second_set])
                result.append(new_set)

    # удаляем пустые множества и преобразовываем в кортеж
    pairs = [tuple(s) for s in result if s]
    pairs.sort(key=lambda x: (x[0], x[1]))


    return pairs
