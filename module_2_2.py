first = int(input("Введите первое число: "))
second = int(input("введите второе число: "))
third = int(input("введите третье число: "))
if first == second and first == third:
    print('совпали все три числа: 3')
elif first == second or first == third or second == third:
    print('совпали двое чисел: 2')
else:
    print('не одно число не совпало: 0')
