# m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']
# m.remove(0.25)
# m.remove(15)
# m.remove('10')
# print(m)

# abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# del abc[1:5]
# print(abc)

# numbers = [1, 4]
# numbers.insert(1,2)
# numbers.insert(2,3)
# print(numbers)

# mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
# del mass[1]
# del mass[7]
# del mass[-6]
# del mass[-2]
# mass.sort()
# print(mass)
# mass.sort(reverse=True)
# print(mass)

# pl=[]
# min=[]
# nul=[]
# count=0
# a=int(input('Кол-во чисел: '))
# for i in range(0,a):
#     b=int(input('Введите число: '))
#     if b<0:
#         min.append(b)
#     if b>0:
#         pl.append(b)
#     if b==0:
#         b='*'
#         nul.append(b)
#         count+=1
# min1=sum(min)
# pl1=sum(pl)/len(pl)
# print(min1)
# print(pl1)
# print('Количество звёздочек:',count, nul)