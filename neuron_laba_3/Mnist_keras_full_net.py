# Загружаем тестовые данные
import keras

from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

# тренеровочный набор - проверочный набор
# train_images, train_labels - Набор для обучения
# test_images -Набор картинок для распознания
# test_labels - Набор названий для проверки
train_images = 'train-images-idx3-ubyte'
train_labels = 'train-labels-idx1-ubyte'
test_images = 't10k-images-idx3-ubyte'
test_labels = 't10k-labels-idx1-ubyte'


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# ------------------
# а давайтие попробуем вывести рандомное число - из обучающего набора , лол
import random
cin_image = train_images[random.randint(1, 60000)]
import matplotlib.pyplot as plt
plt.imshow(cin_image , cmap=plt.cm.binary)
plt.show()
# ------------------
mnist.load_data()


print("Данные загружены")
# Создаем нейронную сеть
network = models.Sequential()

# добавляем входной слой  - изобрадение 28х28 чпикселей
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
# добавляем выходной слой
network.add(layers.Dense(10, activation='softmax'))

# Этап компиляции
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
# Подготовка Исходных данных
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# Подготовка меток

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Начинаем Обучение сети в 5 эпох:
network.fit(train_images, train_labels, epochs=5, batch_size=128)


history_dict = network.history

print(history_dict)
# ---------------------------
#
# # формирование графиков потерь
# import matplotlib.pyplot as plt
# history_dict = network.history
# loss_values = history_dict['loss']
# val_loss_values = history_dict['val_loss']
# acc = history_dict['acc']
#
#
# epochs = range(1, len(acc) + 1)
# plt.plot(epochs, loss_values, 'bo', label='Training loss')
# plt.plot(epochs, val_loss_values, 'b', label='Validation loss')
# plt.title('Training and validation loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()
# plt.show()
#
#
# # формирование графиков точности на этапах обучения и проверки
# acc_values = history_dict['acc']
# val_acc_values = history_dict['val_acc']
# plt.plot(epochs, acc_values, 'bo', label='Training acc')
# plt.plot(epochs, val_acc_values, 'b', label='Validation acc')
# plt.title('Training and validation accuracy')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.legend()
# plt.show()
#

# ---------------------------

# Распзнаем контрольный набор
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc:', test_acc)
print('test_loss' ,test_loss)