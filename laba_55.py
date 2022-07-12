'''
Data Science Jobs Salaries
'''
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Data Science Jobs Salaries.csv')
task1 = df.groupby('employee_residence')['salary_in_usd'].mean()
plt.plot(task1)
plt.show()
task2 = df.groupby('company_location')['salary_in_usd'].mean()
plt.plot(task2)
plt.show()
