def credit_card(c):
    card = [c]
    card_secr = ["************"]
    print(*(card_secr + [card[0][12:]]))


credit_card(input("Введите номер карты: "))


