list1 = [11, 23, 38, 5, 0]
for i in range(1, len(list1)):

    value = list1[i]
    j = i - 1
    while j >= 0 and value < list1[j]:
        list1[j + 1] = list1[j]
        j -= 1
    list1[j + 1] = value
print(list1)
