import json


class IdExistsError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self) -> str:
        return self.message


class YNCheckError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self) -> str:
        return self.message


def read_json():
    with open('__task_14_1_employee.json') as f_load:
        res_dict = json.load(f_load)
        it = iter(res_dict)
        for i in it:
            print(f"[ {i["Id"]}] {i["Name"]}  Role: [{i["Role"]}] "
                  f"{"Working Remote" if i["WorkRemote"] else "Working in Office"}")


def add_json():

    with open('__task_14_1_employee.json') as f_load:
        res_dict = json.load(f_load)

    id_set = set()
    for i in iter(res_dict):
        id_set.add(i["Id"])

    is_exists = True
    id_int = 0
    while is_exists:

        id_str = input("Id: ")

        try:
            id_int = int(id_str)
            if id_int in id_set:
                raise IdExistsError(f"Id {id_str} exists in list of Ids <{tuple(id_set)}>. Try one more time")
            else:
                is_exists = False

        except ValueError:
            print(f"You enter not valid Id: <{id_str}>")
        except IdExistsError as inst_exists:
            print(f"Error: {inst_exists}")

    name = input("Name: ")
    role = input("Role: ")

    yn_check = True
    working_remote = True
    while yn_check:
        working_remote_str = input("Working Remote(Y / N): ").strip()
        try:
            working_remote = False
            match working_remote_str.lower():
                case "y":
                    working_remote = True
                    yn_check = False
                case "n":
                    working_remote = False
                    yn_check = False
                case _:
                    raise YNCheckError(f"You enter not valid: working_remote - <{working_remote_str}>. Try one more time")
        except YNCheckError as inst_check:
            print(f"Error: {inst_check}")

    json_item = {"Id": id_int, "Name": name, "Role": role, "WorkRemote": working_remote}

    res_dict.append(json_item)

    with open('__task_14_1_employee.json', 'w') as f_dump:
        f_dump.write(json.dumps(res_dict, indent=2))


choice = input("1 - read \n2 - add \nEnter your choice: ")

match choice:
    case "1":
        read_json()
    case "2":
        add_json()
    case _:
        print(f"Your choice {choice} is not valid")

