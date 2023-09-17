from typing import List


def recall_at_k(labels: List[int], scores: List[float], k=5) -> float:
    # Сортируем индексы по убыванию скоров
    sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

    # Берем топ-K индексов
    top_k_indices = sorted_indices[:k]

    # Считаем релевантные объекты в топ-K
    num_relevant_in_top_k = sum([1 for i in top_k_indices if labels[i] == 1])

    # Общее количество релевантных объектов
    total_relevant = sum([1 for label in labels if label == 1])

    # Если нет релевантных, возвращаем 0
    if total_relevant == 0:
        return 0.0

    # Возвращаем долю релевантных объектов в топ-K
    return num_relevant_in_top_k / total_relevant


def precision_at_k(labels: List[int], scores: List[float], k=5) -> float:

  # Сортируем индексы по убыванию скоров
    sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

  # Берем топ-K индексов
    top_k_indices = sorted_indices[:k]

  # Считаем релевантные объекты в топ-K
    num_relevant_in_top_k = sum([1 for i in top_k_indices if labels[i] == 1])

  # Возвращаем долю релевантных объектов в топ-K
    return num_relevant_in_top_k / k


def specificity_at_k(labels: List[int], scores: List[float], k=5) -> float:
    # Сортируем индексы по возрастанию скоров
    sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i])

    # Берем последние k индексов
    top_k_indices = sorted_indices[-k:]

    # Считаем отрицательные в топ-K
    num_negatives_in_top_k = sum(1 for i in top_k_indices if labels[i] == 0)

    # Общее кол-во отрицательных
    total_negatives = sum(1 for label in labels if label == 0)

    # Избегаем деления на 0
    if total_negatives == 0:
        total_negatives = 0.00001

    # Возвращаем долю отрицательных
    return num_negatives_in_top_k / total_negatives


def f1_at_k(labels: List[int], scores: List[float], k=5) -> float:
    # Считаем precision@k и recall@k
    precision = precision_at_k(labels, scores, k)
    recall = recall_at_k(labels, scores, k)

    # Проверяем, чтобы знаменатель не был 0
    if precision + recall == 0:
        return 0.0

    # Возвращаем F1-score
    return 2 * (precision * recall) / (precision + recall)
