import pathlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tensorflow as tf
from keras import layers
import keras



# загружаем датасет
# dataset_path = keras.utils.get_file('auto-mpg.data-original', 'auto-mpg.data')
dataset_path = keras.utils.get_file("auto-mpg.data", "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")


# Импортируем его при помощи библиотеки Pandas

column_names = ['Расход топлива','Кол-во цилиндров','Объем двигателя','Л.с.', 'Вес', 'Разгон до 100 км/ч', 'Год выпуска', 'Страна выпуска']
raw_dataset = pd.read_csv(dataset_path, names=column_names, na_values = "?", comment='\t', sep=" ", skipinitialspace=True)
dataset = raw_dataset.copy()
dataset.tail()


# Подготовим данные
dataset.isna().sum()
dataset = dataset.dropna()

# Переводим в числовой текстовые значения
origin = dataset.pop('Страна выпуска')
dataset['США'] = (origin == 1)*1.0
dataset['Европа'] = (origin == 2)*1.0
dataset['Япония'] = (origin == 3)*1.0
dataset.tail()

# РАзделяем данные на тренеровочные и боевые
train_dataset = dataset.sample(frac=0.8,random_state=0)
test_dataset = dataset.drop(train_dataset.index)

# строим графики данных для проверки
sns.pairplot(train_dataset[["Расход топлива", "Кол-во цилиндров", "Объем двигателя", "Вес"]], diag_kind="kde")
train_stats = train_dataset.describe()
train_stats.pop("Расход топлива")
train_stats = train_stats.transpose()
print(train_stats)

# Выделяем целые значения
train_labels = train_dataset.pop('Расход топлива')
test_labels = test_dataset.pop('Расход топлива')
def norm(x):
  return (x - train_stats['mean']) / train_stats['std']
normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)

# ----------------------------------------------------------------------------
#                   Построение самой нейронной сети
#                             пам пам
# ----------------------------------------------------------------------------
def build_model():
  model = keras.Sequential([
    layers.Dense(64, activation=tf.nn.relu, input_shape=[len(train_dataset.keys())]),
    layers.Dense(64, activation=tf.nn.relu),
    layers.Dense(1)
  ])


# Оригинал
#   optimizer = tf.train.RMSPropOptimizer(0.001)
# Жалкая пародия
  optimizer = tf.optimizers.RMSprop(0.001)
#   optimizer = 'rmsprop'

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model



model = build_model()
# Параметр patience определяет количество эпох, проверяемых на улучшение
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)




# Смотрим как выглядит наша модель
model.summary()
example_batch = normed_train_data[:10]
example_result = model.predict(example_batch)
example_result

# Обучение модели
class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

EPOCHS = 1000


history = model.fit(normed_train_data, train_labels, epochs=EPOCHS,
                    validation_split = 0.2, verbose=0, callbacks=[early_stop, PrintDot()])
history_dict = history.history



# Выполним визуализацию процесса обучения при помощи статистики
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()


# Функция визуализации процесса обучения
def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch

  plt.figure()
  plt.xlabel('Эпоха')
  plt.ylabel('Среднее абсолютное отклонение [MPG]')
  plt.plot(hist['epoch'], hist['mae'],
           label='Ошибка при обучении')
  plt.plot(hist['epoch'], hist['val_mae'],
           label = 'Ошибка при проверке')
  plt.ylim([0,5])
  plt.legend()

  plt.figure()
  plt.xlabel('Эпоха')
  plt.ylabel('Среднеквадратическая ошибка [$MPG^2$]')
  plt.plot(hist['epoch'], hist['mse'],
           label='Ошибка при обучении')
  plt.plot(hist['epoch'], hist['val_mse'],
           label = 'Ошибка при проверке')
  plt.ylim([0,20])
  plt.legend()
  plt.show()


plot_history(history)


loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=0)

print("Среднее абсолютное отклонение на проверочных данных: {:5.2f} галлон на милю".format(mae))
# --------------------------------------------------------------------------
#                     Выполнение предсказания
# --------------------------------------------------------------------------
test_predictions = model.predict(normed_test_data).flatten()

plt.scatter(test_labels, test_predictions)
plt.xlabel('Истинные значения [MPG]')
plt.ylabel('Предсказанные значения [MPG]')
plt.axis('equal')
plt.axis('square')
plt.xlim([0,plt.xlim()[1]])
plt.ylim([0,plt.ylim()[1]])
_ = plt.plot([-100, 100], [-100, 100])

error = test_predictions - test_labels
plt.hist(error, bins = 25)
plt.xlabel("Ошибка предскеазаний [MPG]")
_ = plt.ylabel("Количество")
plt.show()