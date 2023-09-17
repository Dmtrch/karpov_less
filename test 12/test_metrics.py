import metrics

def test_profit():
    """Тест функции profit"""
    assert metrics.profit([1, 2, 3], [1, 1, 1]) == 3

def test_margin():
    """Тест функции margin"""
    assert round(metrics.margin([100, 200, 300], [50, 100, 100]), 5) == 0.58333

def test_markup():
    """Тест функции markup"""
    assert round(metrics.markup([100, 200, 300], [50, 100, 100]), 5) == 1.4