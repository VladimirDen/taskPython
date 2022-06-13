class Tomato:
    states = {
        0: "помидора еще нет",
        1: "зеленый",
        2: "средней спелости",
        3: "созрел"
    }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
        if self._state == 1:
            print(f'Помидор {self._index} еще {Tomato.states[self._state]}')
        elif self._state > 1:
            print(f'Помидор {self._index} уже {Tomato.states[self._state]}')

    def is_ripe(self):
        if self._state == 3:
            return True
        return False


class TomatoBush:

    def __init__(self, col):
        self.tomat = [Tomato(index) for index in range(1, col)]

    def grow_all(self):
        for tomato in self.tomat:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomat])

    def give_away_all(self):
        self.tomat = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()
        print(f"Огородник {self.name}, ухаживал за помидорами")

    def harvest(self):
        print('Огородник собирает урожай')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print('Помидоры еще рано собирать')

    @staticmethod
    def knowledge_base():
        print("Сбор помидоров происходит после полного их созревания.\n"
              "Для того чтоб собрать помидоры нужно ввести огородник.harvest().\n"
              "Для того чтоб ухаживать за помидорами нужно ввести огородник.work()")


if __name__ == "__main__":
    Gardener.knowledge_base()
    number_of_tomatoes = TomatoBush(4)
    gardener = Gardener('Vladimir', number_of_tomatoes)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.work()
    gardener.harvest()
