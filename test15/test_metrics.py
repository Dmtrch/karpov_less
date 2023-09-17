import metrics


def test_non_int_clicks():
    try:
        metrics.ctr('a', 2)
    except TypeError:
        pass
    else:
        raise AssertionError("Non int clicks not handled")

    try:
        metrics.ctr([], 2)
    except TypeError:
        pass
    else:
        raise AssertionError("Non int clicks not handled")

    try:
        metrics.ctr(None, 2)
    except TypeError:
        pass
    else:
        raise AssertionError("Non int clicks not handled")

    try:
        metrics.ctr(1.5, 2)
    except TypeError:
        pass
    else:
        raise AssertionError("Non int clicks not handled")

    try:
        metrics.ctr({1}, 2)
    except TypeError:
        pass
    else:
        raise AssertionError("Non int clicks not handled")


def test_non_int_views():
    try:
        metrics.ctr(1, 'b')
    except TypeError:
        pass
    else:
        raise AssertionError("Non int views not handled")

    try:
        metrics.ctr(1, [])
    except TypeError:
        pass
    else:
        raise AssertionError("Non int views not handled")

    try:
        metrics.ctr(1, None)
    except TypeError:
        pass
    else:
        raise AssertionError("Non int views not handled")

    try:
        metrics.ctr(1, 2.5)
    except TypeError:
        pass
    else:
        raise AssertionError("Non int views not handled")

    try:
        metrics.ctr(1, {2})
    except TypeError:
        pass
    else:
        raise AssertionError("Non int views not handled")


def test_non_positive_clicks():
    try:
        metrics.ctr(-1, 2)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative clicks not handled")

    try:
        metrics.ctr(-10, 2)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative clicks not handled")

    try:
        metrics.ctr(-100, 2)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative clicks not handled")

    try:
        metrics.ctr(-1000, 2)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative clicks not handled")


def test_non_positive_views():
    try:
        metrics.ctr(1, -2)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative views not handled")

    try:
        metrics.ctr(1, -20)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative views not handled")

    try:
        metrics.ctr(1, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("Zero views not handled")

    try:
        metrics.ctr(1, -200)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative views not handled")

    try:
        metrics.ctr(1, -2000)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative views not handled")

    try:
        metrics.ctr(-1000, 2)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative clicks not handled")


def test_clicks_greater_than_views():
    try:
        metrics.ctr(10, 5)
    except ValueError:
        pass
    else:
        raise AssertionError("Clicks > views not handled")

    try:
        metrics.ctr(20, 10)
    except ValueError:
        pass
    else:
        raise AssertionError("Clicks > views not handled")

    try:
        metrics.ctr(100, 50)
    except ValueError:
        pass
    else:
        raise AssertionError("Clicks > views not handled")

    try:
        metrics.ctr(200, 100)
    except ValueError:
        pass
    else:
        raise AssertionError("Clicks > views not handled")

    try:
        metrics.ctr(2000, 1000)
    except ValueError:
        pass
    else:
        raise AssertionError("Clicks > views not handled")


def test_zero_views():


    try:
        metrics.ctr(0, 0)
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("Zero views not handled")



