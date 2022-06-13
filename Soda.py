class Soda:
    additive = {
        1: "Чистая",
        2: "Барбарис",
        3: "Малина",
        4: "Ваниль"
    }

    def __init__(self, type):
        self.type = type

    def print_soda(self):
        if self.type in Soda.additive:
            if self.type == 1:
                return "Вы выбрали газировку без наполнителей"
            elif self.type > 1:
                return f"Вы выбрали газировку с наполнителем: {Soda.additive[self.type]}"
        else:
            return "Вы неправильно ввели"

if __name__ == "__main__":
    gas = Soda(int(input("Введите цифру наполнителя для газировки \n"
                         " 1 Чистая\n"
                         " 2 Барбарис\n"
                         " 3 Малина\n"
                         " 4 Ваниль\n"
                         )))
    print(gas.print_soda())
