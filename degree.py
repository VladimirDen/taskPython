def degre(x, n):
    deriv = 1
    for _ in range(n):
        deriv *= x
    return deriv


print("Полученное число:", degre(int(input("Ведите число X:")), int(input("Введите степень в какую нужно возвести число X:"))))
