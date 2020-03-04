from data_base import DataBase
from db_node import DBNode


class TestDataBase(DataBase):
    def __init__(self):
        super(TestDataBase, self).__init__()

    def create_test_data_base(self):
        self.dict = {1: DBNode(0, 1, 'Node_0'),
                     2: DBNode(1, 2, 'Node_1'),
                     3: DBNode(2, 3, 'Node_1_1'),
                     4: DBNode(2, 4, 'Node_1_2'),
                     5: DBNode(2, 5, 'Node_1_3'),
                     6: DBNode(2, 6, 'Node_1_4'),
                     7: DBNode(2, 7, 'Node_1_5'),
                     8: DBNode(1, 8, 'Node_2'),
                     9: DBNode(8, 9, 'Node_2_1'),
                     10: DBNode(8, 10, 'Node_2_2'),
                     11: DBNode(1, 11, 'Node_3'),
                     12: DBNode(1, 12, 'Node_4'),
                     13: DBNode(1, 13, 'Node_5'),
                     14: DBNode(13, 14, 'Node_5_1'),
                     15: DBNode(13, 15, 'Node_5_2'),
                     16: DBNode(15, 16, 'Node_5_2_1'),
                     17: DBNode(15, 17, 'Node_5_2_2'),
                     18: DBNode(13, 18, 'Node_5_3'),
                     19: DBNode(13, 19, 'Node_5_4'),
                     20: DBNode(13, 20, 'Node_5_5'),
                     21: DBNode(20, 21, 'Node_5_5_1'),
                     22: DBNode(20, 22, 'Node_5_5_2'),
                     23: DBNode(22, 23, 'Node_5_5_2_1'),
                     24: DBNode(22, 24, 'Node_5_5_2_2'),
                     25: DBNode(1, 25, 'Node_6'),
                     26: DBNode(25, 26, 'Node_6_1'),
                     27: DBNode(25, 27, 'Node_6_2'),
                     28: DBNode(27, 28, 'Node_6_2_1'),
                     29: DBNode(25, 29, 'Node_6_3'),
                     30: DBNode(25, 30, 'Node_6_4')}
