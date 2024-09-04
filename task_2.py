num = int(input('Введите число: '))
fl = True
print(hex(num))
CONV = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
rez = ''

if num == 0:
    print('0')
    quit()
elif num < 0:
    num = abs(num)
    fl = False

while num > 0:
    rez += CONV[num % 16]
    num //= 16

if fl:
    print(f'0x{rez[::-1]}')
else:
    print(f'-0x{rez[::-1]}')
