def count_after_point(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0

a = input()
b = float(a)
k = 0
n = count_after_point(a)
if int(b) != b:
    while int(b) != b:
        b *= 10
        k += 1
    b -= 1
    while k > 0:
        b /= 10
        k -= 1
    tmp = '{:.' + str(n) + 'f}'
    print(tmp.format(b))
else:
    b -= 10 ** (-n)
    if int(b) == b:
        print(int(b))
    else:
        print(b)