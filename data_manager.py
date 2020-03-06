from cached_tree_controller import CachedTreeController
from db_tree_controller import DBTreeController
from db_node import DBNode


class DataManager:
    def __init__(self, db_controller, cache_controller):
        self.db_controller = db_controller
        self.cache_controller = cache_controller

        self.cache_db_indexes = []

    def reset(self):
        self.db_controller.reset()
        self.cache_controller.reset()

    def load_data_to_cache(self):
        selected_index, selected_item = self.db_controller.selected_item()

        if selected_index is None or selected_item is None:
            return

        new_item_index = self.cache_controller.add_item(selected_item)

        if new_item_index is not None:
            self.cache_db_indexes.append((new_item_index, selected_index))

    def add_new_item_to_cache(self):
        selected_index, selected_item = self.cache_controller.selected_item()

        if selected_index is None or selected_item is None:
            return

        new_item = DBNode(selected_item.node_id)

        new_item_index = self.cache_controller.add_item(new_item)
        self.cache_controller.enter_item_edit_mode(new_item_index)
        print('Added new item to cache')
