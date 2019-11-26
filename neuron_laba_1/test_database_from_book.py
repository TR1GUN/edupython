# Загнрузка тестового набора данных
# все дела
# у меня не работает
import Perceptron
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import decision_regions



# Данные из файла
url = 'iris.data'
df = pd.read_csv(url , header=None)
df.tail()

# ////////////////////////////////////////////////////////////////////
# tail = [[6.7 , 3.0 , 5.2 , 2.3 , "iris virginica" ],
#         [6.3 , 2.5 , 5.0 , 1.9 , "iris virginica" ],
#         [6.5 , 3.0 , 5.2 , 2.0 , "iris virginica" ],
#         [6.2 , 3.4 , 5.4 , 2.3 , "iris virginica" ],
#         [5.9 , 3.0 , 5.1 , 1.8 , "iris virginica" ]]

# ////////////////////////////////////////////////////////////////////
#             Визуализируем полученные даннные с помощтью графика .
#                         пам пам
# ////////////////////////////////////////////////////////////////////

# select setosa and versicolor
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)


X = df.iloc[0:100, [0, 2]].values


plt.scatter(X[:50 , 0], X[:50 , 1],
            color = 'red', marker = 'o', label = 'щетинистый')
plt.scatter(X[50:100 , 0], X[50:100 , 1],
            color = 'blue', marker = 'x', label = 'разноцветный')

plt.xlabel('Длина чашелистника')
plt.ylabel('Длина лепестка')
plt.legend(loc='upper left')
plt.show()

# ////////////////////////////////////////////////////////////////////
#             Теперь натренеруем алгоритм
#                     пам пам
# ////////////////////////////////////////////////////////////////////


ppn = Perceptron.Perceptron(eta =0.1 , n_iter= 10)
ppn.fit(X , y)

# Рисуем график обучения

plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_ , marker= 'o')
plt.xlabel('Эпохи')
# Число ошибочно классифицированых случаев во время обновления обучения
plt.ylabel('Число случаев ошибочной класификации')
plt.show()

# Вспомогательная функция

decision_regions.plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('длина чашелистника')
plt.ylabel('длина лепестка')
plt.legend(loc='upper left')

# показываем
plt.show()
