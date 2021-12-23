import math

rnd = 2 #знаков после запятой

def toratio(n): #перевод десятичной дроби в обыкновенную
    a = n.as_integer_ratio()
    p = int(round(a[1] / a[0], rnd) * 100)
    x = math.gcd(p, 100)
    return 100 // x, p // x

def inp(): #ввод стандартной формы
    x = [1, 1]
    s = input().strip(' ')
    if s[0] == '-':
        x[0] *= -1
        s = s.lstrip('-')
    if s.find('+') != -1:
        s = s.split('+')
    else:
        s = s.split('-')
        x[1] *= -1
    s[0] = s[0].strip(' ')
    s[1] = s[1].strip(' ').strip('i')
    x[0] *= float(s[0])
    x[1] *= float(s[1])
    return x

def inpt(): #ввод тригонометрической формы
    x = input().split(' ')
    return float(x[0]), float(x[1])

def out(z): #вывод стандартной формы
    if z[1] < 0:
        return str(round(z[0], rnd)) + ' - ' + str(round(-1 * z[1], rnd)) + 'i'
    return str(round(z[0], rnd)) + ' + ' + str(round(z[1], rnd)) + 'i'

def outt(z): #вывод тригонометрической формы в радианах
    return str(round(z[0], rnd)) + '(sin' + str(round(z[1], rnd)) + ' + icos' + str(round(z[1], rnd)) + ')'

def outt2(z): #вывод тригонометрической формы в градусах
    return str(round(z[0], rnd)) + '(sin' + str(round(math.degrees(z[1]), rnd))+ '\N{DEGREE SIGN}' \
           + ' + icos' + str(round(math.degrees(z[1]), rnd)) + '\N{DEGREE SIGN}' + ')'

def oute(z): #вывод показательной формы
    return str(round(z[0], rnd)) + 'e^' + str(round(z[1], rnd)) + 'i'

def cn(z): #сопряжённое число
    return z[0], -z[1]

def sm(z, x): #сумма
    return z[0] + x[0], z[1] + x[1]

def df(z, x): #разность
    return z[0] - x[0], z[1] - x[1]

def mp(z, x): #умножение
    return z[0] * x[0] - z[1] * x[1], z[0] * x[1] + z[1] * x[0]

def dv(z, x): #деление
    r = x[0] ** 2 + x[1] ** 2
    z = mp(z, cn(x))
    return z[0] / r, z[1] / r

def tr(z): #трнигонометрическая форма
    r = (z[0] ** 2 + z[1] ** 2) ** 0.5
    g = math.atan2(z[1], z[0])
    return r, g

def ex(z, x): #степень
    y = z
    for i in range(x - 1):
        z = mp(z, y)
    return z

def rt(z, x): #корень
    z = tr(z)
    r = z[0] ** (1/x)
    a = []
    for i in range(x):
        f = ((z[1] + 2 * math.pi * i) / x) % (2 * math.pi)
        a.append([r, f])
    return a

def ts(x): #из тригонометрической формы в радинах в стандартную форму
    return x[0] * math.sin(x[1]), x[0] * math.cos(x[1])

def ts2(x): #из тригонометрической формы в градусах в стандартную форму
    return x[0] * math.sin(math.radians(x[1])), x[0] * math.cos(math.radians(x[1]))

z = inp()
while True:
    c = input()
    if c == '+':
        x = inp()
        z = sm(z, x)
    elif c == '-':
        x = inp()
        z = df(z, x)
    elif c == '*':
        x = inp()
        z = mp(z, x)
    elif c == '/':
        x = inp()
        if x[0] == 0 and x[1] == 0:
            print("You cannot divide by zero")
        else:
            z = dv(z, x)
    elif c == 'c':
        z = cn(z)
    elif c == 't':
        print(outt(tr(z)))
    elif c == 't2':
        print(outt2(tr(z)))
    elif c == '^' or c == '**':
        x = int(input())
        z = ex(z, x)
    elif c == 'r':
        x = int(input())
        for f in rt(z, x):
            print(outt(f))
    elif c == 'r2':
        x = int(input())
        for f in rt(z, x):
            print(outt2(f))
    elif c == 'e':
        print(oute(tr(z)))
    elif c == '0':
        z = inp()
    elif c == 's':
        x = inpt()
        z = ts(x)
    elif c == 's2':
        x = inpt()
        z = ts2(x)
    elif c == 'esc':
        break
    else:
        print('You specified the wrong command')
    print(out(z))
