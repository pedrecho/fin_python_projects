import random

# вывод поля
def out(m):
    print(' |A|B|C|D|E|F|G|H|')
    print('------------------')
    k = 0
    for i in m:
        k += 1
        print(str(k) + '|', end='')
        for l in i:
            if l == 0:
                print(' |', end='')
            else:
                print('@|', end='')
        print()
        print('------------------')

# чей ход
def hod(i):
    if i:
        return 'Первый'
    return 'Второй'

def check1(m, a):
    for i in range(n):
        if m[a][i] == 1:
            return True
    return False

def check2(m, a):
    for i in range(n):
        if m[i][a] == 1:
            return True
    return False

# убрать столбец
def del1(m, k, a):
    for i in range(n):
        k -= m[a][i]
        m[a][i] = 0
    return m, k

# уббрать строку
def del2(m, k, a):
    for i in range(n):
        k -= m[i][a]
        m[i][a] = 0
    return m, k

n = 8 # размер поля от 1 до 9
r = 1 # коэффициент рандома кмани:пустоте = 1:r
k = 0 # счётчик кол-ва оставшихся камней
m = []

# генерация поля
for i in range(n):
    x = []
    for l in range(n):
        x.append(random.randint(0, r) // r)
        k += x[-1]
    m.append(x)

i = False
print('Начало игры')
while k > 0:
    i = not i
    out(m)
    print(hod(i) + ' игрок ходит')
    # print(k)
    a = input().lower()
    if a == 'end':
        print('Игра преждевременно завершена')
        break
    if len(a) > 1:
        print('Невозможный ход')
        i = not i
        continue
    if ord(a) >= ord('a') and ord(a) <= ord('h'):
        if check2(m, ord(a) - ord('a')):
            m, k = del2(m, k, ord(a) - ord('a'))
        else:
            print('Столбец уже пуст')
            i = not i
    elif ord(a) >= ord('1') and ord(a) <= ord(str(n)):
        if check1(m, int(a) - 1):
            m, k = del1(m, k, int(a) - 1)
        else:
            print('Строка уже пуста')
            i = not i
    else:
        print('Неверный ход')
        i = not i
if k == 0:
    print(hod(i)+' игрок победил!')




