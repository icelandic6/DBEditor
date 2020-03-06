from cached_tree_controller import CachedTreeController
from db_tree_controller import DBTreeController
from db_node import DBNode


class DataManager:
    def __init__(self, db_controller, cache_controller):
        self.db_controller = db_controller
        self.cache_controller = cache_controller

        self.__cache_items_index = 1

        self.cached_ids = {}
        self.pre_cached_ids = {}

    def reset(self):
        self.db_controller.reset()
        self.cache_controller.reset()
        self.__cache_items_index = 1

    def load_data_to_cache(self):
        selected_id, selected_item = self.db_controller.selected_item()

        if selected_id is None or selected_item is None:
            return

        if selected_id in self.cached_ids:
            return

        if selected_id in self.pre_cached_ids:
            new_id = self.pre_cached_ids[selected_id]

            self.cached_ids[selected_id] = self.pre_cached_ids[selected_id]
            self.pre_cached_ids.pop(selected_id)
        else:
            new_id = self.__cache_items_index
            self.__cache_items_index += 1

            self.cached_ids[selected_id] = new_id

        new_parent_id = None

        if selected_item.parent_id in self.cached_ids:
            new_parent_id = self.cached_ids[selected_item.parent_id]
        elif selected_item.parent_id in self.pre_cached_ids:
            new_parent_id = self.pre_cached_ids[selected_item.parent_id]

        if new_parent_id is None:
            new_parent_id = self.__cache_items_index
            self.__cache_items_index += 1

            self.pre_cached_ids[selected_item.parent_id] = new_parent_id

            new_item = DBNode(new_parent_id, selected_item.value)

            self.cache_controller.add_item(new_id, new_item)
        else:
            new_item = DBNode(new_parent_id, selected_item.value)

            self.cache_controller.add_item(new_id, new_item)

    def add_new_item_to_cache(self):
        selected_index, selected_item = self.cache_controller.selected_item()

        if selected_index is None or selected_item is None:
            return

        new_item = DBNode(selected_item.node_id)

        new_item_index = self.cache_controller.add_item(new_item)
        self.cache_controller.enter_item_edit_mode(new_item_index)
        print('Added new item to cache')
