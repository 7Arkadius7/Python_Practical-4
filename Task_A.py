# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример: если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = 7
ratio = [randint(0,100) for num in range(k)]
ratio = [str(i) for i in ratio]

n = ['','']                
for i in range(2,k):
    n.append(i)
n = n[::-1]
n = [str(i) for i in n]

x = ['','x']
for i in range(k-2):
        x.append('x**')
x = x[::-1]

m = [' = 0']
for i in range(k):
    m.insert(i,(ratio[i] + x[i] + n[i]))
print(m, '\n')

poly = ''             
for i in range(len(m)):
    if i < len(m)-2:
        poly = poly + m[i] + ' + '
    else:
        poly = poly + m[i]

print(poly)

with open('polynom.txt', 'w+') as data:
    data.write(poly)

data.close()