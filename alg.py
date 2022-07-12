import numpy as np
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
c=input()
f=open(c,'r')
n=list(f.readlines(1))
n=int(n[0].replace('n = ',''))
print(n)
print()
matrix=np.empty((n, n))
for i in range(n):
     strok=f.readlines(i+1)
     for j in range(n):
        strok1=strok[0].split(' ')
        a=convert_to_float(strok1[j])
        matrix[i][j]=a
print(matrix)
lambd=np.empty(n+1)
for i in range(n+1):
    lambd[i]=0
lambd[0]=1
k=0
sum=0
for i in range(n):
    sum+=matrix[i][i]
lambd[1]=sum
for k in reversed(range(2,n)):
    for d in range(n*n):
        for i in range(n-k):
            for j in range(n-k):
                if i+d<n or j+d<n:
                    a = np.empty((n-k,n-k))
                    a[i][j]=matrix[i+d][j+d]
                    lambd[n-k+1]+=det(a,1)
                    print(lambd[n-k+1])
                else:
                    break
lambd[n]=det(matrix,1)
print(lambd[n])
for i in range(n):
    if i%2==0:
        lambd[i]=-lambd[i]
print(lambd)