a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5.45', 'градусов']
i = 0
while i < len(a):
    if a[i][-1].isdigit():
        if float(a[i]) // 10 == 0:
            if len(a[i]) == 1:
                a[i] = '0' + a[i]
            else:
                a[i] = a[i][0] + '0' + a[i][1:]
        a.insert(i, '"')
        a.insert(i+2, '"')
        i += 2
    i += 1
i = 0
while i < len(a):
    if a[i] == '"':
        print(a[i]+a[i+1]+a[i+2], end=' ')
        i += 2
    else:
        print(a[i], end=' ')
    i += 1
