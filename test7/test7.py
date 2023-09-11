import numpy as np

# def turnover_error(y_true: np.array, y_pred: np.array) -> float:
#
#     k = 0.5
#
#     relative_errors = (y_true - y_pred) / y_pred
#
#     squared_errors = relative_errors ** 2
#
#     errors = np.where(relative_errors > 0, squared_errors * k, squared_errors)
#
#     error = np.mean(errors)
#
#     return error
#
# # Example usage
# y_true = np.array([100, 200, 300])
# y_pred = np.array([80, 120, 180])
# error = turnover_error(y_true, y_pred)
# print("True > pred:", error)
#
# y_pred, y_true = y_true, y_pred
# error = turnover_error(y_true, y_pred)
# print("Pred > true", error)

def ltv_error(y_true: np.array, y_pred: np.array) -> float:

    errors = (y_pred ** 2 - y_true ** 2)/y_true**2

    squared_errors = np.where(errors > 0, errors * 2.0,
                              abs(errors * 2))
    mean_error = np.mean(squared_errors)

    return mean_error

# Example usage
y_true = np.array([10000, 15000, 20000])
y_pred = np.array([12000, 14000, 18000])
error = ltv_error(y_true, y_pred)
print("LTV error:", error)