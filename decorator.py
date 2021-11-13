def decorator(dec):
    def tru():
        if dec() <= 0:
            if dec() == 81:
                return dec() / 9
            return
        return dec() * 2


@decorator
def dec(2, 5):
    return a * b


