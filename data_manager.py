from cached_tree_controller import CachedTreeController
from db_tree_controller import DBTreeController


class DataManager:
    def __init__(self, db_controller, cache_controller):
        self.db_controller = db_controller
        self.cache_controller = cache_controller

        self.cache_db_indexes = []

    def reset(self):
        self.db_controller.reset()
        self.cache_controller.reset()

    def load_data_to_cache(self):
        index, item = self.db_controller.selected_item()

        if index is None or item is None:
            return

        new_item_index = self.cache_controller.add_item(item)

        if new_item_index is not None:
            self.cache_db_indexes.append((new_item_index, index))

    def add_new_item_to_cache(self):
        self.cache_controller.add_new_node()
