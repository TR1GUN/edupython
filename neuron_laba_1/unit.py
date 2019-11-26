import Perceptron
import pandas as pd
url = 'iris.data'
df = pd.read_csv(url , header=None)
df.tail()

print(df, type(df))

