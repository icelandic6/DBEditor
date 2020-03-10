from core.db_item import DBItem
from core.data_manager_actions import ItemActionEnum, ItemAction


class DataManager:
    def __init__(self, db_controller, cache_controller):
        self.__db_controller = db_controller
        self.__cache_controller = cache_controller

        self.__cache_items_id = 1

        self.__new_cached_items = {}

        self.__cached_ids = {}
        self.__pre_cached_ids = {}

        self.__item_actions = []

        self.__cache_controller.item_edited.connect(self.on_cache_item_edited)

    def reset(self):
        self.__db_controller.reset()
        self.__cache_controller.reset()
        self.__cached_ids.clear()
        self.__pre_cached_ids.clear()
        self.__item_actions.clear()
        self.__new_cached_items.clear()
        self.__cache_items_id = 1

    def load_data_to_cache(self):
        selected_id, selected_item = self.__db_controller.selected_item()

        if selected_id is None or selected_item is None:
            return

        if selected_id in self.__cached_ids:
            return

        if selected_id in self.__pre_cached_ids:
            new_id = self.__pre_cached_ids[selected_id]

            self.__cached_ids[selected_id] = self.__pre_cached_ids[selected_id]
            self.__pre_cached_ids.pop(selected_id)
        else:
            new_id = self.__cache_items_id
            self.__cache_items_id += 1

            self.__cached_ids[selected_id] = new_id

        new_parent_id = None

        if selected_item.parent_id in self.__cached_ids:
            new_parent_id = self.__cached_ids[selected_item.parent_id]
        elif selected_item.parent_id in self.__pre_cached_ids:
            new_parent_id = self.__pre_cached_ids[selected_item.parent_id]

        if new_parent_id is None:
            new_parent_id = self.__cache_items_id
            self.__cache_items_id += 1

            self.__pre_cached_ids[selected_item.parent_id] = new_parent_id

            new_item = DBItem(new_parent_id, selected_item.value)

            self.__cache_controller.add_item(new_id, new_item)
        else:
            new_item = DBItem(new_parent_id, selected_item.value)

            added_item_exists = self.__cache_controller.add_item(new_id, new_item)

            if not added_item_exists:
                self.__cache_controller.remove_item(new_id)

    def add_new_item_to_cache(self):
        selected_id, selected_item = self.__cache_controller.selected_item()

        if selected_id is None or selected_item is None:
            return

        new_item = DBItem(selected_id)

        new_id = self.__cache_items_id
        self.__cache_items_id += 1

        self.__cache_controller.add_item(new_id, new_item)
        self.__cache_controller.enter_item_edit_mode(new_id)

        self.__new_cached_items[new_id] = new_item

        self.__item_actions.append(ItemAction(new_id,  ItemActionEnum.action_item_add))

    def remove_cache_item(self):
        selected_id, selected_item = self.__cache_controller.selected_item()

        if selected_id is None or selected_item is None:
            return

        self.__cache_controller.remove_item(selected_id)

        self.__item_actions.append(ItemAction(selected_id, ItemActionEnum.action_item_remove))

    def edit_cache_item(self):
        selected_id, selected_item = self.__cache_controller.selected_item()

        if selected_id is None or selected_item is None:
            return

        self.__cache_controller.enter_item_edit_mode(selected_id)

    def on_cache_item_edited(self, item_id, value):
        self.__item_actions.append(ItemAction(item_id, ItemActionEnum.action_item_edit))

    def get_db_id(self, cache_id):
        for k, v in self.__cached_ids.items():
            if v == cache_id:
                return k

        return None

    def apply_changes(self):
        for action in self.__item_actions:
            if action.action == ItemActionEnum.action_item_add:
                item = self.__new_cached_items.get(action.item_id)

                if not item:
                    continue

                db_parent_id = self.get_db_id(item.parent_id)

                if not db_parent_id:
                    for k, v in self.__pre_cached_ids.items():
                        if v == item.parent_id:
                            db_parent_id = k

                # if not db_parent_id and item.parent_id in self.__new_cached_items:
                #     db_parent_id = self.__new_cached_items[item.parent_id]

                if not db_parent_id:
                    continue

                new_item = DBItem(db_parent_id, item.value)

                new_item_id = self.__db_controller.add_new_item(new_item)

                self.__cached_ids[new_item_id] = action.item_id
            elif action.action == ItemActionEnum.action_item_remove:
                db_id = self.get_db_id(action.item_id)

                if db_id:
                    self.__db_controller.remove_item(db_id)

            elif action.action == ItemActionEnum.action_item_edit:
                db_id = self.get_db_id(action.item_id)

                cached_item = self.__cache_controller.get_item(action.item_id)

                if not cached_item or not db_id:
                    continue

                self.__db_controller.edit_item(db_id, cached_item.value)

        self.__item_actions.clear()
