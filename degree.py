def degre(x, n):
    deriv = 1
    for _ in range(n):
        deriv *= x
    return deriv

x = int(input("Ведите число X:"))
n = int(input("Введите степень в какую нужно возвести число X:"))
print("Полученное число:", degre(x, n))