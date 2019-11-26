# Реализация персептрона ,
# Инициализируется новые обьекты персептрон
# можно задавать :
# темп обучения - eta
# количество эпох - проходов по числовому набору - n_integer

import numpy as np


class Perceptron(object):
    """"Классификатор на основе персептрона.

    Параметры :
    eta - float  Темп обучения (  между 0.0 и 1.0)

    n_inter - int - проходы по тренеровочному заданию

  um  Атрибуты:

    w_ - одномерный массив - Весовые коофициенты после подгонки

    errors_ - список - число ошибочной классификации в каждой эпохе
    """

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter


# с помощью метода выполняем подгонку
# инициализируем нужные веса w_

    def fit(self, X, y):
        """
        DВыполнить подгонку модели под тренеровочные данные
        Параментры :
        :param X: массивоподобный , форма : {n_samples , n_features}
        тренеровояные векторы , где:
        n_samples - число образцов
        n_features - число признаков

        :param y: массивоподобный , форма:
        целевые значения
        Возвращает :
        self - object
        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self
# вычесление скалярного произведения вектора весов
    def net_input(self, X):
        """рассчитать считый вход """

        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        " Вернуть метку класса после единичного скачка "
        return np.where(self.net_input(X) >= 0.0, 1, -1)



