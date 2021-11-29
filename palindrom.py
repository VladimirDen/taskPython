def palindrom(word):

    if word == word[::-1]:
        print("Слово является палиндромом.")
    else:
        print("Слово не является палиндромом.")


if __name__ == "__main__":
    palindrom(input("Ведите слово: ").casefold())
