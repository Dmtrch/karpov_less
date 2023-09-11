import numpy as np

def turnover_error(y_true: np.array, y_pred: np.array) -> float:

    k = 0.5

    relative_errors = (y_true - y_pred) / y_pred

    squared_errors = relative_errors ** 2

    errors = np.where(relative_errors > 0, squared_errors * k, squared_errors)

    error = np.mean(errors)

    return error