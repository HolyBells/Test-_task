data = {}  # микро бд с работниками
numb = '0123456789'


def insert():  # внесение в бд работников(построчно) с дальнейшим выводом
    while True:
        word = input().split()
        if word and len(word) == 2 and word[0] not in numb:  # проверка на цифры и пробелы
            if word[0] not in data:
                data[word[0]] = [int(word[1])]  # создание нового работника
            else:
                data[word[0]].append(int(word[1]))  # добавление к существующему работнику
        else:
            break

    for key, value in data.items():  # вывод в виде "имя, кол-во часов, сумма часов"
        return f"{key}: {', '.join(map(str, value))}: sum: {sum(value)}"


print(insert())  # после вызова нужно вводить имя и количество часов в одну строку, отделять работников клавишей Enter,
# пустая строка будет означать окончание ввода
