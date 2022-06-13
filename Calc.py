print("Чтоб завершить работу калькулятолра введите 00")
while True:
    s = input("Введите знак операции какую нужно выполнить(+,-,*,/,factorial): ")
    if s == '00':
        break
    if s in ('+', '-', '*', '/', 'faktorial'):
        x = float(input("Введите первое значение a="))
        y = float(input("Введите второе значение b="))
        if s == '+':
            print(a + b)
        elif s == '-':
            print(a - b)
        elif s == '*':
            print(a * b)
        elif s == '/':
            if y != 0:
                print(a / b)
            else:
                print("Делить на ноль нельзя!")
        elif s == "factorial"
            def factorial(n):
                if n == 0:
                    return 1
            else:
            return n * factorial(n - 1)

    else:
        print("Неверный знак операции!")