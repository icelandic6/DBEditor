class DataBase:
    def __init__(self):
        self._dict = {}

    def has_item(self, item_id):
        return item_id in self._dict

    def get_item(self, item_id):
        return self._dict.get(item_id, None)

    def get_items(self):
        return self._dict.items()

    def get_data(self):
        return self._dict.copy()

    def get_ids(self):
        return self._dict.keys()

    def add_item(self, item_id, item):
        self._dict[item_id] = item

    def edit_item(self, item_id, value):
        if item_id in self._dict:
            self._dict[item_id].value = value

    def get_new_id(self):
        return max(self._dict, key=int) + 1

    def clear(self):
        self._dict.clear()
