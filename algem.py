import numpy as np
#Рекурсивный алгоритм расчёта определителя матрицы
def det(matrix,mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        answer = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            answer = answer + mul * det(m, sign * matrix[0][i])
    return answer
#Перевод дробей к типу float
def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        try:
            num, denom = frac_str.split('/')
        except ValueError:
            return None
        try:
            leading, num = num.split(' ')
        except ValueError:
            return float(num) / float(denom)
        if float(leading) < 0:
            sign_mult = -1
        else:
            sign_mult = 1
        return float(leading) + sign_mult * (float(num) / float(denom))
#Открытие файла и чтение 1 строки
c=input()
f=open(c,'r')
n=list(f.readlines(1))
n=int(n[0].replace('n = ',''))
# создание марицы и чтение этиой матрицы
matrix=np.empty((n, n))
for i in range(n):
     strok=f.readlines(i+1)
     for j in range(n):
        strok1=strok[0].split(' ')
        a=convert_to_float(strok1[j])
        matrix[i][j]=a
#создание массива под значения полинома
lambd=np.empty(n+1)
for i in range(n+1):
    lambd[i]=0
#коэф при 1 члене равен 1
lambd[0]=1
k=0
sum=0
#2-ой элемент находим как tr(matrix)
for i in range(n):
    sum+=matrix[i][i]
lambd[1]=sum
#вычисления значений членов характеристического многочлена
for k in reversed(range(2,n)):
    for d in range(n*n):
        for i in range(n-k):
            for j in range(n-k):
                if i+d<n and j+d<n:
                    a = np.empty((n-k,n-k))
                    a[i][j]=matrix[i+d][j+d]
                    lambd[n-k+1]+=det(a,1)
                else:
                    break
#нахождение С из характеристического многочлена
lambd[n]=det(matrix,1)
#вывод
print('Matrix:')
print(matrix)
for i in range(n):
    if i%2==0:
        lambd[i]=-lambd[i]
F=''
for i in range(n+1):
    if lambd[i]<=0:
        if n-i == 0:
            F += str(lambd[i])
            continue
        F += str(lambd[i])+'x^'+str(n-i)
    else:
        F += '+'+ str(lambd[i]) + 'x^' + str(n-i)
print('F(x)=',F)
print('Rational eigenvalues:')
# простите за нампи, по другому не получалось(((( За это анекдот:В дверь постучались i раз
#sqrt(-1)-подумал Штирлец)))))
strok=list(np.roots(lambd))
for i in range(len(strok)):
    print('x_'+str(i)+' = '+'%.3f'%strok[i])
