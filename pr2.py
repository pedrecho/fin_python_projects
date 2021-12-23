import re

# всякая сложная генерация базовыхх элементов
signs = ['плюс', 'минус', 'умножить', 'скобкаоткрывается', 'скобказакрывается']
d = ['ноль', '', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
     'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
     'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать',
     'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
numbers = []
for i in range(8):
    for l in range(10):
        numbers.append(d[21 + i] + d[1 + l])
numberst = d[:1] + d[2:21] + numbers + ['']
numberst2 = d[:1] + d[2:21]
for i in range(8):
    for l in range(10):
        numberst2.append(d[21 + i] + ' ' + d[1 + l])
# print(numberst[70])
numbers += d[:1] + d[11:21] + d[2:11]
# print(numbers)


# выполнение математического действия s над элементами a и b
def action(a, b, s):
    if s == signs[0]:
        return a + b
    if s == signs[1]:
        return a - b
    if s == signs[2]:
        return a * b

def calc(string):

    wr = "Некорректный ввод"
    string = ''.join(string.split())
    print(string)
    if string.count(signs[3]) != string.count(signs[4]):
        return wr
    while string.count(signs[3]) > 0:
        l = string.rfind(signs[3])
        r = string.find(signs[4], l)
        if r == -1 or l + len(signs[3]) == r:
            return wr
        cl = calc(string[l + len(signs[3]):r])
        if cl == wr:
            return wr
        string = string[:l] + cl + string[r + len(signs[4]):]

    # получение массива чисел
    s = ''
    for i in signs:
        s += i + '|'
    s = s[:-1]
    # print(s)
    number = re.split(s, string)
    print(number)
    for i in range(len(number)):
        if number[i] in numberst:
            number[i] = numberst.index(number[i])
        else:
            return wr
    print(number)

    # получение массива действий
    s = ''
    for i in numbers:
        s += i + '|'
    s = s[:-1]
    # print(s)
    sign = re.split(s, string)[1:-1]
    print(sign)


    if len(number) != len(sign) + 1:
        return wr

    # выполняем действия
    while sign.count('умножить') > 0:
        f = sign.index('умножить')
        number[f] = action(number[f], number[f + 1], sign[f])
        del number[f + 1]
        del sign[f]
    # print(number)

    while len(number) > 1:
        number[0] = action(number[0], number[1], sign[0])
        del number[1]
        del sign[0]
    if number[0] < 0:
        return wr
        # return signs[1] + ' ' + numberst[number[0] * -1]
    return numberst2[number[0]]


print(calc(input().lower()))
