import tensorflow as tf

import tensorflow_datasets as tfds

# from tensorflow.examples.tutorials.mnist import input_data
# mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
mnist = tfds.image.mnist

# включяаем режим для немедленного выполнения
# tf.enable_eager_execution()

# размерность вектора


vector_dimension = 784

# Задаем переменную для тренеровочных данных
# x - сам тензор , 784 - число сторон векторов для обучения производной длины - none
x = tf.placeholder(tf.float32 , [None , vector_dimension])

 # Переменные для изменения весов
#  W - перемножаем вектор с возможными метками  -
# количество проходов - 10
# если чего - заменить переменной , но это не точно
W = tf.Variable(tf.zerros(([vector_dimension , 10])))
b = tf.Variable(tf.zerros([10]))
# --------------------------------------------------------------------------------
#           Добавляем скрытый слой
# --------------------------------------------------------------------------------
W_relu = tf.Variable(tf.truncated_normal([784, 100], stddev=0.1))
b_relu = tf.Variable(tf.truncated_normal([100], stddev=0.1))


# --------------------------------------------------------------------------------
# записываем модель :

y = tf.nn.softmax(tf.matmul(x, W) +b)

# записываем способ для проверки качества предсказаний
# -заглушка
y_ = tf.placeholder(tf.float32 , [None , 10])
# сама функция потерь
cross_entropy =tf.reduce_mean(
    -tf.reduce_sum(y_ * tf.log(y) , reduction_indices =[1])
)
# скорость обучения модели :
speed_education = 0.5

train_step = tf.train.GradientDescentOptimizer(speed_education).minimize(cross_entropy)


# Инициализируем
init = tf.initialize_global_variables()

# запускаем сессию

sess = tf.Session()
sess.run(init)

# запускаем
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# корректность предсказаний

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print("Точность: %s" %
    sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
