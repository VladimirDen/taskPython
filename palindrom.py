def palindrom(word):

    if word == word[::-1]:
        print("Слово является палиндромом.")
    else:
        print("Слово не является палиндромом.")


palindrom(input("Ведите слово: "))
