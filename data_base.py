class DataBase:
    def __init__(self):
        self.dict = {}

    def find_node_by_id(self, node_id):
        if node_id in self.dict:
            return self.dict[node_id]

        return None
