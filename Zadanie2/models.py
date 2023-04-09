import json


class Costs:
    def __init__(self):
        try:
            with open("costs.json", "r") as f:
                self.costs = json.load(f)
        except FileNotFoundError:
            self.costs = []

    def all(self):
        return self.costs

    def get(self, id):
        return self.costs[id]

    def create(self, data):
        data.pop('csrf_token')
        self.costs.append(data)

    def save_all(self):
        with open("costs.json", "w") as f:
            json.dump(self.costs, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.costs[id] = data
        self.save_all()


costs = Costs()