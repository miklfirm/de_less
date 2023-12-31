from pprint import pprint
import yaml
import json
import pandas

# -----------------------------------------
class User:
    id: int
    name: str
    nickname: str
    age: int
    balance: float

    def __init__(self, id, name, nickname, age, balance):
        self.id = id
        self.name = name
        self.nickname = nickname
        self.age = age
        self.balance = balance

    def print_users(self):
        pprint([self.id, self.name, self.nickname, self.age, self.balance])
# -----------------------------------------
class Users:
    user: list

    def __init__(self, list_users):
        self.user = list_users

    def pushUsers(self, user):
        self.user.append(user)

    def getUsers(self):
        for element in self.user:
           element.print_users()
# -----------------------------------------
class Users_dict:
    users: list

    def __init__(self, dict_users):
        self.users = dict_users

    def setUsersInFileYaml(self):
        with open(r'users.yaml', 'w') as file:
          yaml.dump(self.users, file)

    def getUsersInFileYaml(self):
        with open(r'users.yaml', 'r') as file:
            pprint(yaml.load(file, Loader=yaml.FullLoader))

    def setUsersInFileCSV(self):
        df = pandas.DataFrame(self.users)
        df.to_csv("users.csv",index=False)

    def getUsersInFileCSV(self):
        df = pandas.read_csv("users.csv")
        print(df)

    def setUsersInFileJSON(self, filename):
        with open(filename, 'w') as file:
          file.write(json.dumps(self.users, indent=4))

    def getUsersInFileJSON(self, filename):
        with open(filename, 'r') as file:
            pprint(json.load(file))
            # json.dumps(self.users, indent=4)
    def getUsers(self):
        pprint(self.users)

    def YamlToJson(self):
        with open("users.yaml", 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            with open("users_yaml_to_json.json", 'w') as file2:
                file2.write(json.dumps(data, indent=4))

    def JsonToYaml(self):
        with open("users.json", 'r') as file:
           data = json.load(file)
           with open("users_json_to_yaml.yaml", 'w') as file2:
                yaml.dump(data, file2)

# ---------------------------------------------------
my_users = [
    {
        "id": "1",
        "name": "miklushov",
        "nickname": "mikl",
        "age": "34",
        "balance": "146.5"
    },
    {
        "id": "2",
        "name": "ivanov",
        "nickname": "boba",
        "age": "30",
        "balance": "0.0"
    },
    {
        "id": "3",
        "name": "petrov",
        "nickname": "pipka",
        "age": "33",
        "balance": "100"
    },
]
filename = "users.json"
dict_users2 = Users_dict(my_users)
# dict_users2.getUsers()
# dict_users2.setUsersInFileYaml()
# dict_users2.getUsersInFileYaml()
# dict_users2.setUsersInFileJSON(filename)
# dict_users2.getUsersInFileJSON(filename)
# dict_users2.setUsersInFileCSV()
# dict_users2.getUsersInFileCSV()
dict_users2.YamlToJson()
dict_users2.JsonToYaml()
print("-------list----------")
list_users_old = [User(1, "miklushov","mikl",34, 146.5),
                  User(2, "ivanov","boba",30, 0.0),
                  User(3, "petrov","pipka",33, 100)]

all_users = Users(list_users_old)

# all_users.getUsers()

