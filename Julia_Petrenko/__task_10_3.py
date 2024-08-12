class HistoryList:
    history = {"add": [], "del": []}
    __lst = []

    @classmethod
    def add_value(cls, val):
        cls.__lst.append(val)
        cls.history["add"].append(val)

    @classmethod
    def del_value(cls, ind):
        if -len(cls.__lst) <= ind < len(cls.__lst):
            cls.history["del"].append(cls.__lst.pop(ind))

    @classmethod
    def get_value(cls, ind):
        if -len(cls.__lst) <= ind < len(cls.__lst):
            return cls.__lst[ind]

    @property
    def data(self):
        return tuple(self.__lst)

    @property
    def addition_history(self):
        return tuple(self.history["add"])

    @property
    def deletion_history(self):
        return tuple(self.history["del"])

    def get_history(self):
        return {"add": tuple(self.history["add"]), "del": tuple(self.history["del"])}


my_list = HistoryList()

my_list.add_value(10)
my_list.add_value(20)
my_list.add_value(30)
my_list.add_value(20)

my_list.del_value(-4)
my_list.del_value(1)

print(f"data: {my_list.data}")
print(f"addition_history: {my_list.addition_history})")
print(f"deletion_history: {my_list.deletion_history}")
print(f"get_value: {my_list.get_value(-2)}")
print(f"get_history(): {my_list.get_history()}")



        
