def minn(a, b, c):
    mins = a
    if mins >= b:
        b, mins = mins, b
    elif mins >= c:
        c, mins = mins, c
    return mins
 
    
print("Введите три числа")
a = int(input("Первое:"))
b = int(input("Еще одно:"))
c = int(input("Ну и последнее:"))
print("Минимальное из их:", minn(a, b, c))