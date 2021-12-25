string = input("Введите число через пробелы - ").split()
for i, word in enumerate(string,1):
    print(f'{i}, {word[:10]}')