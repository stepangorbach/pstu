from random import randint as random #импорт функции генерации случайных чисел

def task1():
    randomNumber = random(100,999)
    print(randomNumber)
    randomNumber = str(randomNumber)
    a = int(randonNumber[0])
    b = int(randonNumber[1])
    c = int(randonNumber[2])
    print(a, b ,c)
    if (a+b+c)%2 == 0:
        print("Сумма цифр числа", randomNumber, "является четным числом")
    else:
        print("Сумма цифр числа", randomNumber, "не является четным числом")

def task2():
    floor = random(10,99); print("количество этажей:", floor); print("количество квартир:", floor*3)
    flat = random(1, floor*3); print("номер случайной квартиры:", flat)
    flatOnFloor = flat//3; print("номер этажа квартиры:", flatOnFloor)
    if flatOnFloor%2==1:
        print("лифт поднимется  на этаж", flatOnFloor)
    else:
        print("лифт поднимется на этаж", flatOnFloor+1)

task1()
task2()