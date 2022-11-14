def output(prices):
    e = ', '
    for i in range(len(prices)):
        r, k = prices[i].split('.')
        if len(k) < 2:
            k = '0' + k
        if i == len(a) - 1:
            e = ''
        print(f'{r} руб {k} коп', end=e)
    print()


a = list('88.00 55.27 92.21 12.46 17.03 25.26 84.85 27.25 86.47 82.52 72.89 73.30 56.42 65.03 5.71 36.05\
 5.79 76.08 15.01 72.97'.split())
output(a)
a.sort()
output(a)
b = list(reversed(a))
output(b)
c = b[:5]
output(list(reversed(c)))
