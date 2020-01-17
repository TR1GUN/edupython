from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras import utils
from keras.preprocessing import image
# from google.colab import files
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random
from keras.models import load_model
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Список с названиями классов
classes = ['футболка', 'платье', 'свитер', 'брюки', 'пальто', 'туфли', 'рубашка', 'кроссовки', 'сумка', 'ботинки']
model = load_model('fashion_mnist.h5')
# model = load_model('fashion_mnist_dense_v2.h5')

print(model.summary())

# -----------------------------------------------------------
# -----------------------------------------------------------
# Попытаемся загрузить картинку
img_path = 'trousers.png'
img = image.load_img(img_path, target_size=(28, 28), color_mode = "grayscale")
plt.imshow(img.convert('RGBA'))
plt.show()
# Преобразуем картинку для обработки нейронной сетью

# Преобразуем картинку в массив
x = image.img_to_array(img)
# Меняем форму массива в плоский вектор
x = x.reshape(1, 784)
# Инвертируем изображение
x = 255 - x
# Нормализуем изображение
x /= 255

# Запускаем распознавание

prediction = model.predict(x)

print(prediction)

# Выводим результаты распознавания
prediction = np.argmax(prediction[0])
print("Номер класса:", prediction)
print("Название класса:", classes[prediction])
