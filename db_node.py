class DBNode:
    def __init__(self, parent_id, node_id, value=''):
        self.node_id = node_id
        self.parent_id = parent_id
        self.value = value
