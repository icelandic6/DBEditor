from enum import Enum


class ItemActionEnum(Enum):
    action_item_add = 1
    action_item_remove = 2
    action_item_edit = 3


class ItemAction:
    def __init__(self, item_id, item_action: ItemActionEnum):
        self.item_id = item_id
        self.action = item_action
