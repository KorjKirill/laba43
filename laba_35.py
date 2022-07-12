'''
Лаба номер 35
'''
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Cleaned_Laptop_data.csv')
df1 = df.sort_values(by="brand")
task1 = df.groupby('brand')['model'].count().sort_values(ascending=True)
print(task1)
plt.plot(task1)
plt.show()
task2 = df.groupby('os')['model'].count().sort_values(ascending=True)
print(task2)
plt.plot(task2)
plt.show()
