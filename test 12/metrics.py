from typing import List


def profit(revenue: List[float], costs: List[float]) -> float:
    return sum(revenue) - sum(costs)


# def margin(revenue: List[float], costs: List[float]) -> float:
#     return (sum(revenue) - sum(costs)) / sum(revenue)
#
#
# def markup(revenue: List[float], costs: List[float]) -> float:
#     return (sum(revenue) - sum(costs)) / sum(costs)

def margin(revenue: List[float], costs: List[float]) -> float:
    if sum(revenue) == 0:
        return 0.0
    return (sum(revenue) - sum(costs)) / sum(revenue)


def markup(revenue: List[float], costs: List[float]) -> float:
    if sum(costs) == 0:
        return 0.0
    return (sum(revenue) - sum(costs)) / sum(costs)