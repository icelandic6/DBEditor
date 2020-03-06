from data_base import DataBase
from db_node import DBNode


class TestDataBase(DataBase):
    def __init__(self):
        super(TestDataBase, self).__init__()

    def create_test_data_base(self):
        self.dict = {1: DBNode(0, 'Node_0'),
                     2: DBNode(1, 'Node_1'),
                     3: DBNode(2, 'Node_1_1'),
                     4: DBNode(2, 'Node_1_2'),
                     5: DBNode(2, 'Node_1_3'),
                     6: DBNode(2, 'Node_1_4'),
                     7: DBNode(2, 'Node_1_5'),
                     8: DBNode(1, 'Node_2'),
                     9: DBNode(8, 'Node_2_1'),
                     10: DBNode(8, 'Node_2_2'),
                     11: DBNode(1, 'Node_3'),
                     12: DBNode(1, 'Node_4'),
                     13: DBNode(1, 'Node_5'),
                     14: DBNode(13, 'Node_5_1'),
                     15: DBNode(13, 'Node_5_2'),
                     16: DBNode(15, 'Node_5_2_1'),
                     17: DBNode(15, 'Node_5_2_2'),
                     18: DBNode(13, 'Node_5_3'),
                     19: DBNode(13, 'Node_5_4'),
                     20: DBNode(13, 'Node_5_5'),
                     21: DBNode(20, 'Node_5_5_1'),
                     22: DBNode(20, 'Node_5_5_2'),
                     23: DBNode(22, 'Node_5_5_2_1'),
                     24: DBNode(22, 'Node_5_5_2_2'),
                     25: DBNode(1, 'Node_6'),
                     26: DBNode(25, 'Node_6_1'),
                     27: DBNode(25, 'Node_6_2'),
                     28: DBNode(27, 'Node_6_2_1'),
                     29: DBNode(25, 'Node_6_3'),
                     30: DBNode(25, 'Node_6_4')}
