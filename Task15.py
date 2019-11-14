num = int(input('Введите Ваш возраст:'))
if num % 2 == 0:
    for age in range(0, num + 1, 2):
        print(age)
else:
    for yo in range(1, num + 1, 2):
        print(yo)