def insert_poly(file, poly, d):
    with open(file, 'r') as data:
        poly = data.read()
    poly = poly.replace(' = 0','')
    poly = poly.split(' + ')
    poly = poly[::-1]
    
    for i, elem in enumerate(poly):
        if elem.isdigit():
            d[i] = int(elem)
        else:
            d[i] = int(elem.partition('x')[0])
    return d

d1 = {}
d2 = {}
polynom1 = ''
polynom2 = ''
file1 = 'poly1.txt'
file2 = 'poly2.txt'
insert_poly(file1, polynom1, d1)
insert_poly(file2, polynom2, d2)
print(d1)
print(d2,'\n')

if len(d2) < len(d1):
    diff = len(d1) - len(d2)
    for i in range(len(d2), len(d2) + diff):
        d2[i] = 0

elif len(d1) < len(d2):
    diff = len(d2) - len(d1)
    for i in range(len(d1), len(d1) + diff):
        d1[i] = 0



for i in d1:
    d1[i] = d1[i] + d2[i]
print(f'Результат сложения словарей: {d1}\n')


polynomial = []
for key, value in d1.items():
    if key> 0:
        polynomial.append(str(value) + 'x**' + str(key) +' + ')
    elif key == 0:
        polynomial.append(str(value) + ' = 0')
polynomial = polynomial[::-1]


polynomial = ''.join(polynomial)
print(polynomial)


with open ('poly_result.txt','w+') as file:
    file.write(polynomial)

file.close()