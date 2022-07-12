'''
Лаба номер 15
'''
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('coursera_data.csv')
df1=df.groupby('course_difficulty')['course_students_enrolled'].count().sort_values(ascending=True)
print(df1)
plt.plot(df1)
plt.show()
df2=df.groupby('course_difficulty')['course_rating'].mean().sort_values(ascending=True)
print(df2)
plt.plot(df2)
plt.show()
