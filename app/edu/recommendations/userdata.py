import json

class UserData:
    uinform = 'app/source/data/users_information.json'

    def __init__(self):
        self.read_info()

    def read_info(self, id=1):
        with open(self.uinform, 'r') as f:
            self.information = json.load(f)

    def get_skills(self, id=1):
        return self.information['skills']

    def get_tasks(self, id=1):
        return self.information['task']

