import numpy as np

def smape(y_true: np.array, y_pred: np.array) -> float:

    res_smape = np.zeros_like(y_true)

    delta = (abs(np.min(y_true + y_pred)) + 1)/2
    y_true = np.add(y_true, delta)
    y_pred = np.add(y_pred, delta)

    up_dev = 2 * np.abs(y_true - y_pred)
    dn_dev = np.abs(y_true) + np.abs(y_pred)
    f_t = dn_dev != 0

    res_smape[f_t] = up_dev[f_t] / dn_dev[f_t]
    return np.mean(res_smape)