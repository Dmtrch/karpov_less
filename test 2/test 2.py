import numpy as np


# def smape(y_true: np.array, y_pred: np.array) -> float:
#     a = np.mean(2 * np.abs(y_true - y_pred) / (np.abs(y_true) + np.abs(y_pred)))
#     return a


def smape1(y_true: np.array, y_pred: np.array) -> float:

    res_smape = np.zeros_like(y_true)

    delta = (abs(np.min(y_true + y_pred)) + 1)/2
    y_true = np.add(y_true, delta)
    y_pred = np.add(y_pred, delta)

    up_dev = 2 * np.abs(y_true - y_pred)
    dn_dev = np.abs(y_true) + np.abs(y_pred)
    f_t = dn_dev != 0

    res_smape[f_t] = up_dev[f_t] / dn_dev[f_t]
    b = np.mean(res_smape)
    return b


def smape2(y_true: np.array, y_pred: np.array) -> float:
    res_smape = np.zeros_like(y_true)

    up_dev = 2 * np.abs(y_true - y_pred)
    dn_dev = np.abs(y_true) + np.abs(y_pred)
    f_t = dn_dev != 0

    res_smape[f_t] = up_dev[f_t] / dn_dev[f_t]
    b = np.mean(res_smape)
    return b

# def smape3(y_true: np.array, y_pred: np.array) -> float:
#
#     res_smape = np.zeros_like(y_true)
#
#     y_true = np.array(y_true)
#     y_pred = np.array(y_pred)
#
#     true_tmp = np.log(y_true + 1)
#     pred_tmp = np.log(y_pred + 1)
#
#     up_dev = 2 * np.abs(y_true - y_pred)
#     dn_dev = np.abs(y_true) + np.abs(y_pred)
#     f_t = dn_dev != 0
#
#     res_smape[f_t] = up_dev[f_t] / dn_dev[f_t]
#     b = np.mean(res_smape)
#     return b

# np.random.seed(42)  # Для воспроизводимости случайных значений
y_true = np.random.uniform(-1,1,1000)  # Пример случайных значений для y_true
y_pred = np.random.uniform(-1,1,1000)  # Пример случайных значений для y_pred

y_true[2] = 0
y_pred[2] = 0

# print("sMAPE:", smape(y_true, y_pred))
print("smape1", smape1(y_true,y_pred))
print("smape2", smape2(y_true,y_pred))
# print("smape3", smape3(y_true,y_pred))
