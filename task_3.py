CONV = {
        1000:'M', 900:'СM', 500:'D', 400:'CD',
        100:'C', 90:'XC', 50:'L', 40:'XL',
        10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I',
        }

num = int(input('Введите число от -3999 до 3999: '))
rez = ''

print(f'Римское представление числа "{num}" : ', end='')

if num <= 0:
    num = abs(num)
    rez = '-'

for key, value in CONV.items():
    while num >= key:
        num -= key
        rez += value

print(rez)