def nod(x, y):
    for i in range(y, 0, -1):
        if x % i == 0 and y % i == 0:
            return (f'НОД: {i}')

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

if num_1 == num_2:
    print(f'НОД: {num_1}')
elif num_1 < num_2:
    if num_2 % num_1 == 0:
        print(f'НОД: {num_1}')
    else:
        print(nod(num_2, num_1))
else:
    if num_1 % num_2 == 0:
        print(f'НОД: {num_2}')
    else:
        print(nod(num_1, num_2))