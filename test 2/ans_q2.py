import numpy as np
def smape(y_true: np.array, y_pred: np.array) -> float:

    f_t = np.abs(y_true) + np.abs(y_pred) != 0
    res_smape = np.zeros_like(y_true)
    res_smape[f_t] = (2 * np.abs(y_true - y_pred)[f_t]) / (np.abs(y_true)[f_t] + np.abs(y_pred)[f_t])

    return np.mean(res_smape)