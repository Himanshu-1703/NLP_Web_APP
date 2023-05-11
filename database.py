import json


class DataBase:

    def insert_into_db(self, email, username, password):

        # read the json file
        with open(file='users.json', mode='r') as rf:
            users = json.load(rf)

            if email in users:
                return False
            else:
                users[email] = [username, password]

        # write the object to file
        with open(file='users.json', mode='w') as wf:
            json.dump(users, wf)

        return True

    def check_login(self, email, password):
        with open(file='users.json', mode='r') as rf:
            users = json.load(rf)

            if email in users:
                if password == users[email][1]:
                    return True
                else:
                    return False
            else:
                return False

    def get_profile(self, email):
        with open(file='users.json', mode='r') as rf:
            users = json.load(rf)

        return users[email][0]

    def insert_api(self, email, key):
        with open(file='users.json', mode='r') as rf:
            users = json.load(rf)

        if len(users[email]) == 2:
            val = users[email]
            val.append(key)
            users[email] = val

        else:
            val = users[email]
            val[2] = key
            users[email] = val

        with open(file='users.json', mode='w') as wf:
            json.dump(users, wf)

        return True

    def get_api(self, email):
        with open(file='users.json', mode='r') as rf:
            users = json.load(rf)

            if len(users[email]) == 3:
                key = users[email][2]
                return key

            else:
                return ''
