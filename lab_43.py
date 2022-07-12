'''
Лаба номер 43
'''
import pandas as pd
import matplotlib.pyplot as plt
gate1=[0]*1000
df = pd.read_csv('StudentsPerformance.csv')
task1 = df.groupby('race/ethnicity')['math score'].mean()
gate=df['test preparation course']
for i in range(1000):
    if gate[i]=='none':
        gate1[i]=0
    else:
        gate1[i]=1
df['test']=gate1
task2 = df.groupby('race/ethnicity')['test'].mean()
#0, если студент не готовился,1 если готовился. Расчёт среднего показателя по группе
plt.plot(task1)
plt.show()
print(task2)
plt.plot(task2)
plt.show()
