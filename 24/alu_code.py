def monad_digit0(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 14
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 7
    y *= x
    z += y
    return x, y, z


def monad_digit1(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 12
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 4
    y *= x
    z += y
    return x, y, z


def monad_digit2(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 11
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 8
    y *= x
    z += y
    return x, y, z


def monad_digit3(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += -4
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 1
    y *= x
    z += y
    return x, y, z


def monad_digit4(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 10
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 5
    y *= x
    z += y
    return x, y, z


def monad_digit5(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 10
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 14
    y *= x
    z += y
    return x, y, z


def monad_digit6(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 15
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 12
    y *= x
    z += y
    return x, y, z


def monad_digit7(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += -9
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 10
    y *= x
    z += y
    return x, y, z


def monad_digit8(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += -9
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 5
    y *= x
    z += y
    return x, y, z


def monad_digit9(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 12
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 7
    y *= x
    z += y
    return x, y, z


def monad_digit10(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += -15
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 6
    y *= x
    z += y
    return x, y, z


def monad_digit11(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += -7
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 8
    y *= x
    z += y
    return x, y, z


def monad_digit12(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += -10
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 4
    y *= x
    z += y
    return x, y, z


def monad_digit13(w, x, y, z):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += 0
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 6
    y *= x
    z += y
    return x, y, z


def monad(number):
    x = 0
    y = 0
    z = 0
    x, y, z = monad_digit0(int(number[0]), x, y, z)
    x, y, z = monad_digit1(int(number[1]), x, y, z)
    x, y, z = monad_digit2(int(number[2]), x, y, z)
    x, y, z = monad_digit3(int(number[3]), x, y, z)
    x, y, z = monad_digit4(int(number[4]), x, y, z)
    x, y, z = monad_digit5(int(number[5]), x, y, z)
    x, y, z = monad_digit6(int(number[6]), x, y, z)
    x, y, z = monad_digit7(int(number[7]), x, y, z)
    x, y, z = monad_digit8(int(number[8]), x, y, z)
    x, y, z = monad_digit9(int(number[9]), x, y, z)
    x, y, z = monad_digit10(int(number[10]), x, y, z)
    x, y, z = monad_digit11(int(number[11]), x, y, z)
    x, y, z = monad_digit12(int(number[12]), x, y, z)
    x, y, z = monad_digit13(int(number[13]), x, y, z)
    print('MONAD: model number: {}, z = {}'.format(number, z))


monad('29599469991739')
monad('17153114691118')
