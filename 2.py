workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in workers:
    name = i.split()[-1]
    name = name.lower()
    name = name.capitalize()
    print(f'Привет, {name}!')
