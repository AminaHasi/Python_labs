# Гасимова Аміна 141 група
# Лабороторна робота №1
# 15. Дано змінні A, B, C. Змінити їх значення, перемістивши вміст A в B, B - в C, C - в A, і вивести
# нові значення змінних A, B, C.


def moving_val(val1, val2, val3):
    val1, val2, val3 = val2, val3, val1
    return val1, val2, val3


a = float(input("Введіть A: "))
b = float(input("Введіть B: "))
c = float(input("Введіть C: "))
print(moving_val(a, b, c))
