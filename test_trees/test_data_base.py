from core.data_base import DataBase
from core.db_item import DBItem


class TestDataBase(DataBase):
    def __init__(self):
        super(TestDataBase, self).__init__()

    def create_test_data_base(self):
        self._dict = {1: DBItem(0, 'Node_0'),
                      2: DBItem(1, 'Node_1'),
                      3: DBItem(2, 'Node_1_1'),
                      4: DBItem(2, 'Node_1_2'),
                      5: DBItem(2, 'Node_1_3'),
                      6: DBItem(2, 'Node_1_4'),
                      7: DBItem(2, 'Node_1_5'),
                      8: DBItem(1, 'Node_2'),
                      9: DBItem(8, 'Node_2_1'),
                      10: DBItem(8, 'Node_2_2'),
                      11: DBItem(1, 'Node_3'),
                      12: DBItem(1, 'Node_4'),
                      13: DBItem(1, 'Node_5'),
                      14: DBItem(13, 'Node_5_1'),
                      15: DBItem(13, 'Node_5_2'),
                      16: DBItem(15, 'Node_5_2_1'),
                      17: DBItem(15, 'Node_5_2_2'),
                      18: DBItem(13, 'Node_5_3'),
                      19: DBItem(13, 'Node_5_4'),
                      20: DBItem(13, 'Node_5_5'),
                      21: DBItem(20, 'Node_5_5_1'),
                      22: DBItem(20, 'Node_5_5_2'),
                      23: DBItem(22, 'Node_5_5_2_1'),
                      24: DBItem(22, 'Node_5_5_2_2'),
                      25: DBItem(1, 'Node_6'),
                      26: DBItem(25, 'Node_6_1'),
                      27: DBItem(25, 'Node_6_2'),
                      28: DBItem(27, 'Node_6_2_1'),
                      29: DBItem(25, 'Node_6_3'),
                      30: DBItem(25, 'Node_6_4')}
