import fractions

def nod(x, y):
    for i in range(y, 0, -1):
        if x % i == 0 and y % i == 0:
            return (i)


str_1 = input('Введите первую дробь: ')
str_2 = input('Введите вторую дробь: ')

print(f'Ответ:\n{str_1} * {str_2} = ', end='')

str_1 = str_1.split('/')
str_2 = str_2.split('/')

zn = int(str_1[0]) * int(str_2[0])
dell = int(str_1[1]) * int(str_2[1])
curr_nod = nod(zn, dell)

print(f'{zn}/{dell} = ', end='')

while curr_nod != 1:
    zn //= curr_nod
    dell //= curr_nod
    curr_nod = nod(zn, dell)

if dell == 1:
    print(f'{zn}\n')
else:
    print(f'{zn}/{dell}\n')

print(f'Проверка с помощью модуля fractions:')

d1 = fractions.Fraction(int(str_1[0]), int(str_1[1]))
d2 = fractions.Fraction(int(str_2[0]), int(str_2[1]))

print(f'Сумма {d1 + d2}\nПроизведение: {d1 * d2}')

