from keras.models import load_model
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



model =load_model('fashion_mnist_dense_v2.h5')

# Запускаем сеть на входных данных

prediction = model.predict(x_test)
# Визуализируем все это
n = random.randint(0, 10)
plt.imshow(x_test[n].reshape(28, 28), cmap=plt.cm.binary)
plt.show()



# выводим один из результатов предсказания

print(prediction[n])

# Выводим номер класса предсказанный нейросетью

print(np.argmax(prediction[n]))
print(classes[np.argmax(prediction[n])])

# выводим правильный ответ
print(np.argmax(y_test[0]))

print(classes[np.argmax(y_test[n])])