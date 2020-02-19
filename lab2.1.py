from random import randint as random

def show(x):
    for i in range(len(x[0])):
        print(x[i])

def show_reverse(x):
    print("\nMATRIX.REVERSE()")
    for i in range(len(x[0])):
        x[i].reverse(); print(x[i])

def task1(x):
    print("\n-----------TASK 1-----------")
    array = [random(0,100) for i in range(x)]
    print(array); array.reverse(); print(array, "\n")

def task2(x):
    print("\n-----------TASK 2-----------")
    #xyList = [random(-10, 10) for i in range(2*x)]
    xyList = [i for i in range(2*x)]
    point = [0 for i in range(6)]
    long = [0 for i in range(3)]
    xList = []; yList = []
    number = str(" ")
    n = 0; num = []

    for i in range(2*x):
        if i%2 == 0:
            xList.append(xyList[i])
        else:
            yList.append(xyList[i])
            
    print("X+Y: ", xyList)
    print("X: ", xList)
    print("Y: ", yList)
    print("points: ", point)

    for i in range(len(xList)):
        point[0] = xList[i]
        point[1] = yList[i]
        for j in range(1, len(xList)):
            if j == i:
                continue
            point[2] = xList[j]
            point[3] = yList[j]
            for k in range(2, len(xList)):
                if i == k or j == k:
                    continue
                n += 1
                point[4] = xList[k]
                point[5] = yList[k]

                long[0] = round(((((point[2] - point[0]) ** 2) + ((point[3] - point[1]) ** 2)) ** 0.5), 2)
                long[1] = round(((((point[4] - point[2]) ** 2) + ((point[5] - point[3]) ** 2)) ** 0.5), 2)
                long[2] = round(((((point[4] - point[0]) ** 2) + ((point[5] - point[1]) ** 2)) ** 0.5), 2)
                print("\nAB, BC, AC: ", long)

                print('\nШАГ ', n)
                print('A: ', point[0:2])
                print('B: ', point[2:4])
                print('C: ', point[4:6])

                if long[0] == long[1] or long[0] == long[2] or long[1] == long[2]:
                    number = str("ШАГ ") + str(n) + str(" ") + str("A: ") + str(i+1) + str(" ") + str("B: ") + str(j+1) + str(" ") + str("C: ") + str(k+1)
                    num.append(number)
                    print("\nОбновлен список номеров удовлетворяющих условию:\n", num)
    
    print("\n")

def task3(x):
    print("\n-----------TASK 3-----------")
    matrix = []
    for i in range(x):
        matrix.append([0]*x)
    idX = 0; idY = 0; k = x
    j = 1; n = 1
    for l in range(x):
        if j == 1:
            print("\nШАГ",l+1," ДЕЙСТВИЕ1")
            for i in range(k):
                matrix[idY][idX] = n
                idY += 1; idX += 1; n += 1
            idX -= 2; idY -= 1; k -= 1
            show(matrix)
            j = 2

        elif j == 2:
            print("\nШАГ",l+1," ДЕЙСТВИЕ2")
            for i in range(k):
                matrix[idY][idX] = n
                idX -= 1; n += 1
            idX += 1; idY -= 1; k -= 1
            show(matrix)
            j = 3

        elif j == 3:
            print("\nШАГ",l+1," ДЕЙСТВИЕ3")
            for i in range(k):
                matrix[idY][idX] = n
                idY -= 1; n += 1
            idX += 1; idY += 2; k -= 1
            show(matrix)
            j = 1
    
    print("\n")
    show(matrix)
    show_reverse(matrix)
    
task1(10)
task2(4)
task3(int(input("INPUT YOUR MATRIX SIZE: ")))
