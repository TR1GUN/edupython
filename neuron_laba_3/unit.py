from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Dense
from keras import utils
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import random
# Загружаем данные
(x_train , y_train) , (x_test , y_test ) = fashion_mnist.load_data()


# Название класов одежды

classes = ['Футболка','Брюки','Свитер','Платье','Пальто','Туфли','Рубашка','Кросовки','Сумка','Ботнки']


# ---------- Просматриваем примеры изображений --------------
plt.figure(figsize=(10,10))
for i in range(100,150):
    plt.subplot(5,10,i-100+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap=plt.cm.binary)
    plt.xlabel(classes[y_train[i]])

# --------------------------------------------------------------



# Преообразование размерности избраженний

x_train = x_train.reshape(60000 , 784)
# Нормализация данных
x_train = x_train / 255

# Преобразцуем метки в категории
y_train = utils.to_categorical(y_train, 10)

# Создаем последовательную модель
model = Sequential()

# Добавляем слоев

model.add(Dense(800 , input_dim=784, activation= 'relu'))
model.add(Dense(10 , activation= 'softmax'))
# Компилируем модель -  градиентный спуск , ошибка - энтропия - метрика качества - доля правильных ответов
model.compile (loss = "categorical_crossentropy" ,
               optimizer="SGD" , metrics=["accuracy"])

# печатаем параметры нашей нейронной сети

print (model.summary())



# ///////////////////////////////////////////////////////
# # Компилируем модель
# model.compile (loss = "categorical_crossentropy" ,
#                optimizer="adam" , metrics=["accuracy"])



# Обучаем модель

model.fit(x_train, y_train , batch_size=200,  epochs = 100 , validation_split=0.2, verbose=1)
# ///////////////////////////////////////////////////////
# # Сохраняем модель
#
model.save('fashion_mnist.h5')
#
# # ///////////////////////////////////////////////////////

# Запускаем сеть на входных данных

prediction = model.predict(x_train)
# Визуализируем все это
n = random.randint(0, 10)
plt.imshow(x_train[n].reshape(28, 28), cmap=plt.cm.binary)
plt.show()



# выводим один из результатов предсказания

print(prediction[n])

# Выводим номер класса предсказанный нейросетью

print(np.argmax(prediction[n]))
print(classes[np.argmax(prediction[n])])

# выводим правильный ответ
print(np.argmax(y_train[0]))

print(classes[np.argmax(y_train[n])])