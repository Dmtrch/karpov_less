import numpy as np

def ltv_error(y_true: np.array, y_pred: np.array) -> float:

    errors = abs(y_pred ** 2 - y_true ** 2)/y_true**2

    squared_errors = np.where(errors > 0, errors * 2.0,
                                            abs(errors) )
    mean_error = np.mean(squared_errors)

    return np.sqrt(mean_error)



