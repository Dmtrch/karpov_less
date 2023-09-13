import utils


def test_word_count():
    """Проверка подсчёта слов в одном наборе текстов."""

    texts = ["one two three", "four five six"]
    count = utils.word_count(texts)

    assert count == {'one': 1, 'two': 1, 'three': 1,
                     'four': 1, 'five': 1, 'six': 1}


def test_word_count_tricky():
    """Проверка, что результаты не перезаписываются между вызовами."""

    batch1 = ["one two three", "four five six"]
    count1 = utils.word_count(batch1)

    batch2 = ["one one one", "two three three"]
    count2 = utils.word_count(batch2)

    assert count1 != count2
