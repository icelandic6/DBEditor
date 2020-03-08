class DataBase:
    def __init__(self):
        self.dict = {}

    def get_item_by_id(self, item_id):
        return self.dict.get(item_id, None)
