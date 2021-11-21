class Mail:
    def __init__(self, name, znak, domen):
        if name.isalnum():
            self.name = name
        elif not name.isalnum():
            print("Вы ввели неправилное значение, в этом поле могут присутствовать буквы и цифры кроме (/ * - + \ . , ; : #)")
        elif znak == "@":
            self.znak = znak
        elif znak != '@':
            print("Вы ввели неправилное значение! Здесь должен быть символ @")
        elif "." in str(domen):
            self.domen = domen
        elif "." not in str(domen):
            print("Неправильно должно выглядеть так gmail.com")
        else:
            print("Error")

    def __str__(self):
        return f"{self.name}{self.znak}{self.domen}"

if __name__ == "__main__":

    i = Mail("dfna1", "@", "gmail.com")
    print(i)
