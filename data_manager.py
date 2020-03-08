from db_node import DBNode

from enum import Enum


class ItemActionEnum(Enum):
    action_item_add = 1
    action_item_remove = 2
    action_item_edit = 3


class ItemAction:
    def __init__(self, item_id, item_action:ItemActionEnum):
        self.item_id = item_id
        self.action = item_action


class DataManager:
    def __init__(self, db_controller, cache_controller):
        self.db_controller = db_controller
        self.cache_controller = cache_controller

        self.__cache_items_id = 1

        self.__new_cached_items = {}

        self.cached_ids = {}
        self.pre_cached_ids = {}

        self.item_actions = []

        self.cache_controller.item_edited.connect(self.on_cache_item_edited)

    def reset(self):
        self.db_controller.reset()
        self.cache_controller.reset()
        self.cached_ids.clear()
        self.pre_cached_ids.clear()
        self.item_actions.clear()
        self.__new_cached_items.clear()
        self.__cache_items_id = 1

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
            new_id = self.__cache_items_id
            self.__cache_items_id += 1

            self.cached_ids[selected_id] = new_id

        new_parent_id = None

        if selected_item.parent_id in self.cached_ids:
            new_parent_id = self.cached_ids[selected_item.parent_id]
        elif selected_item.parent_id in self.pre_cached_ids:
            new_parent_id = self.pre_cached_ids[selected_item.parent_id]

        if new_parent_id is None:
            new_parent_id = self.__cache_items_id
            self.__cache_items_id += 1

            self.pre_cached_ids[selected_item.parent_id] = new_parent_id

            new_item = DBNode(new_parent_id, selected_item.value)

            self.cache_controller.add_item(new_id, new_item)
        else:
            new_item = DBNode(new_parent_id, selected_item.value)

            self.cache_controller.add_item(new_id, new_item)

    def add_new_item_to_cache(self):
        selected_id, selected_item = self.cache_controller.selected_item()

        if selected_id is None or selected_item is None:
            return

        new_item = DBNode(selected_id)

        new_id = self.__cache_items_id
        self.__cache_items_id += 1

        self.cache_controller.add_item(new_id, new_item)
        self.cache_controller.enter_item_edit_mode(new_id)

        self.__new_cached_items[new_id] = new_item

        self.item_actions.append(ItemAction(new_id, ItemActionEnum.action_item_add))

    def remove_cache_item(self):
        selected_id, selected_item = self.cache_controller.selected_item()

        if selected_id is None or selected_item is None:
            return

        self.cache_controller.remove_item(selected_id)

        self.item_actions.append(ItemAction(selected_id, ItemActionEnum.action_item_remove))

    def edit_cache_item(self):
        selected_id, selected_item = self.cache_controller.selected_item()

        if selected_id is None or selected_item is None:
            return

        self.cache_controller.enter_item_edit_mode(selected_id)

    def on_cache_item_edited(self, item_id, value):
        self.item_actions.append(ItemAction(item_id, ItemActionEnum.action_item_edit))

    def get_db_id(self, cache_id):
        for k, v in self.cached_ids.items():
            if v == cache_id:
                return k

        return None

    def apply_changes(self):
        for action in self.item_actions:
            if action.action == ItemActionEnum.action_item_add:
                item = self.__new_cached_items.get(action.item_id)

                if not item:
                    continue

                db_parent_id = self.get_db_id(item.parent_id)

                if not db_parent_id:
                    for k, v in self.pre_cached_ids.items():
                        if v == item.parent_id:
                            db_parent_id = k

                # if not db_parent_id and item.parent_id in self.__new_cached_items:
                #     db_parent_id = self.__new_cached_items[item.parent_id]

                if not db_parent_id:
                    continue

                new_item = DBNode(db_parent_id, item.value)

                new_item_id = self.db_controller.add_new_item(new_item)

                self.cached_ids[new_item_id] = action.item_id
            elif action.action == ItemActionEnum.action_item_remove:
                db_id = self.get_db_id(action.item_id)

                if db_id:
                    self.db_controller.remove_item(db_id)

            elif action.action == ItemActionEnum.action_item_edit:
                db_id = self.get_db_id(action.item_id)

                cached_item = self.cache_controller.get_item(action.item_id)

                if not cached_item or not db_id:
                    continue

                self.db_controller.edit_item(db_id, cached_item.value)

        self.item_actions.clear()
