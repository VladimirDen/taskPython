def credit_card(card):
    print("*" * 12 + str(card[12:]))


if __name__ == "__main__":
    credit_card(input("Введите номер карты: "))
