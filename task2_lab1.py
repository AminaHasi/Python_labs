# Гасимова Аміна 141 група
# Лабороторна робота №1
# 10. Даний розмір файла в байтах. Використовуючи операцію ділення без залишку, знайти кількість
# повних кілобайтів, які займає даний файл (1 кілобайт = 1024 байта)


def file_size(x):
    return x//1024


bait = int(input("Введііть розмір файла в байтах: "))
result = file_size(bait)
print(result)
