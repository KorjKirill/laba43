'''
Лаба номер 43
'''
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance.csv')
task1 = df.groupby('parental level of education')['reading score'].mean()
plt.plot(task1)
plt.show()
task2 = df.groupby('parental level of education')['writing score'].min()
plt.plot(task2)
plt.show()
