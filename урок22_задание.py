class Resume:
    def __init__(self, newName, newAge, newfavProgLang):
        Resume.name = newName
        Resume.age = newAge
        Resume.fav_prog_lang = newfavProgLang

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, newAge):
        self.__age = newAge

    @property
    def fav_prog_lang(self):
        return self.__favProglang

    @fav_prog_lang.setter
    def fav_prog_lang(self, newfavProgLang):
        self.__favProglang = newfavProgLang


class ResumePlus(Resume):
    def __init__(self, newposition, newPlaceofWork, newName, newAge, newfavProgLang):
        ResumePlus.position = newposition
        ResumePlus.place_of_work = newPlaceofWork
        super().__init__(newName, newAge, newfavProgLang)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, newposition):
        self.__position = newposition

    @property
    def place_of_work(self):
        return self.__position

    @place_of_work.setter
    def place_of_work(self, newPlaceofWork):
        self.__place_of_work = newPlaceofWork

    def __str__(self):
        return f"{ResumePlus.position}, {ResumePlus.place_of_work}, {super().name}, {super().age}, {super().fav_prog_lang}"


if __name__ == "__main__":
    I = Resume("Vladimir", 36, "Python")
    print(I.name)
    Inew = ResumePlus("Минск", "developer", "Vladimir", 36, "Python")
    print(Inew)