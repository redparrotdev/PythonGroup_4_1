

class Singletone(type):

    __instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)

        return self.__instance


class Player(metaclass=Singletone):

    def __init__(self):
        self.x = 10


p1 = Player()
print(p1)

p2 = Player()
print(p1)

p2.x = 20




