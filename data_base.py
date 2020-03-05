class DataBase:
    def __init__(self):
        self.dict = {}

    def get_node_by_index(self, element_index):
        return self.dict.get(element_index, None)
