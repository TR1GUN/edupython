from keras.datasets import fashion_mnist
from keras.models import Sequential

from keras import layers
from keras.layers import Dense, Dropout , Flatten
from keras import utils
from keras.preprocessing import image
# from google.colab import files
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random
# Загружаем набор данных
# (x_train, y_train) - набор данных для обучения
# (x_test, y_test) - набор данных для тестирования
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Список с названиями классов
classes = ['футболка', 'брюки', 'свитер', 'платье', 'пальто', 'туфли', 'рубашка', 'кроссовки', 'сумка', 'ботинки']

# --------------------------
# Просматриваем примеры изображений
plt.figure(figsize=(10,10))
for i in range(100,150):
    plt.subplot(5,10,i-100+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap=plt.cm.binary)
    plt.xlabel(classes[y_train[i]])
# -------------------------
# Преобразование размерности данных в наборе
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# Векторизованные операции
# Применяются к каждому элементу массива отдельно
x_train = x_train / 255
x_test = x_test / 255

# Работа с правильными ответами


n = random.randint(0,20)
print(y_train[n])
y_train = utils.to_categorical(y_train, 10)
y_test = utils.to_categorical(y_test, 10)
print(y_train[n])



# Создаем последовательную модель
model = Sequential()
# Входной полносвязный слой, 800 нейронов, 784 входа в каждый нейрон

model.add(Dense(256, activation="relu"))
model.add(Dense(128, activation="relu"))
# Выходной полносвязный слой, 10 нейронов (по количеству рукописных цифр)
model.add(Dense(10, activation="softmax"))
# Компилируем сеть
model.compile(loss="categorical_crossentropy", optimizer="Adam", metrics=["accuracy"])
print(model.summary())

# Обучаем нейронную сеть
history = model.fit(x_train, y_train,
                    batch_size=200,
                    epochs=100,
                    validation_split=0.2,
                    verbose=1)
# Сохраняем
model.save('fashion_mnist_dense_v2.h5')
# Проверка качества работы на наборе данных для тестирования
scores = model.evaluate(x_test, y_test, verbose=1)
print("Доля верных ответов на тестовых данных, в процентах:", round(scores[1] * 100, 4))

# Используем сеть для распознавания предметов одежды

n_rec = 496

plt.imshow(x_test[n_rec].reshape(28, 28), cmap=plt.cm.binary)
plt.show()
# Меняем размерность изображения и нормализуем его
x = x_test[n_rec]
x = np.expand_dims(x, axis=0)

# Запускаем распознавание
prediction = model.predict(x)

# Выводим результаты распознавания
prediction = np.argmax(prediction[0])
print("Номер класса:", prediction)
print("Название класса:", classes[prediction])


# Печатаем правильный ответ

label = np.argmax(y_test[0])

print('правильный ответ')
print("Номер класса:", label)
print("Название класса:", classes[label])

# Загружаем свою картинку

