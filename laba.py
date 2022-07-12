import pandas as pd
import matplotlib.pyplot as plt
gate1=[0]*8
df = pd.read_csv('hurricanes.csv')
task1=df.transpose()
print(task1)
plt.plot(task1)
plt.show()
task2 = df.groupby('company_location')['salary_in_usd'].mean()
plt.plot(task2)
plt.show()