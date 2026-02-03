import json
class DatasetLoader:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        with open(self.filename, "r") as f:
            data = json.load(f)
            return data
        
    def filter_by_user(self, inputuser_id):
            data = self.load()
            result = []
            for line in data:
                if line["user_id"] == inputuser_id:
                    result.append(line)
            return result

file = DatasetLoader("day06/events.json")
file.load()
print(file.filter_by_user(101))