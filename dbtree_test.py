import dbnode


class DBTreeTest():
    def __init__(self):
        self.root = None

    def create_test_tree(self):
        self.root = dbnode.DBNode('Node0')

        node1 = self.root.add_child('Node1')
        node11 = node1.add_child('Node11')
        node12 = node1.add_child('Node12')
        node13 = node1.add_child('Node13')
        node14 = node1.add_child('Node14')
        node15 = node1.add_child('Node15')
        node16 = node1.add_child('Node16')

        node2 = self.root.add_child('Node2')
        node21 = node2.add_child('Node21')
        node22 = node2.add_child('Node22')
        node221 = node22.add_child('Node221')
        node222 = node22.add_child('Node222')
        node223 = node22.add_child('Node223')
        node23 = node2.add_child('Node23')
        node24 = node2.add_child('Node24')
        node25 = node2.add_child('Node25')

        node3 = self.root.add_child('Node3')

        node4 = self.root.add_child('Node4')

        node5 = self.root.add_child('Node5')
        node51 = node5.add_child('Node51')
        node52 = node5.add_child('Node52')
        node521 = node52.add_child('Node521')
        node522 = node52.add_child('Node522')
        node5221 = node522.add_child('Node5221')
        node5222 = node522.add_child('Node5222')
        node53 = node5.add_child('Node53')
        node531 = node53.add_child('Node531')
        node532 = node53.add_child('Node532')

        node6 = self.root.add_child('Node6')
        node61 = node6.add_child('Node61')
        node62 = node6.add_child('Node62')
        node621 = node62.add_child('Node621')
        node622 = node62.add_child('Node622')
        node623 = node62.add_child('Node623')
        node624 = node62.add_child('Node624')
        node625 = node62.add_child('Node625')
        node6251 = node625.add_child('Node6251')
        node6252 = node625.add_child('Node6252')
        node62521 = node6252.add_child('Node62521')
        node62522 = node6252.add_child('Node62522')
        node62523 = node6252.add_child('Node62523')
        node62524 = node6252.add_child('Node62524')
        node62525 = node6252.add_child('Node62525')
        node6253 = node625.add_child('Node6253')
        node63 = node6.add_child('Node63')
        node64 = node6.add_child('Node64')
        node65 = node6.add_child('Node65')
        node66 = node6.add_child('Node66')
        node661 = node66.add_child('Node661')
        node662 = node66.add_child('Node662')
        node663 = node66.add_child('Node663')
        node664 = node66.add_child('Node664')
        node665 = node66.add_child('Node665')
        node6651 = node665.add_child('Node6651')
        node6652 = node665.add_child('Node6652')
        node66521 = node6652.add_child('Node66521')
        node66522 = node6652.add_child('Node66522')
        node66523 = node6652.add_child('Node66523')
        node6653 = node665.add_child('Node6653')
        node6654 = node665.add_child('Node6654')
        node6655 = node665.add_child('Node6655')
        node6656 = node665.add_child('Node6656')

        node7 = self.root.add_child('Node7')

        node8 = self.root.add_child('Node8')
        node81 = node8.add_child('Node81')
        node82 = node8.add_child('Node82')
        node83 = node8.add_child('Node83')
        node84 = node8.add_child('Node84')
        node85 = node8.add_child('Node85')
        node86 = node8.add_child('Node86')
        node87 = node8.add_child('Node87')
        node871 = node87.add_child('Node871')
        node872 = node87.add_child('Node872')
        node873 = node87.add_child('Node873')
        node874 = node87.add_child('Node874')
        node875 = node87.add_child('Node875')
        node876 = node87.add_child('Node876')
        node877 = node87.add_child('Node877')
        node878 = node87.add_child('Node878')
        node88 = node8.add_child('Node88')
        node89 = node8.add_child('Node89')

        node9 = self.root.add_child('Node9')
        node91 = node9.add_child('Node91')
        node92 = node9.add_child('Node92')

    def print_tree(self):
        print('TREE\n\n')

        spacing = 0

        self.print_node(self.root, spacing)

    def print_node(self, node, spacing):
        spacing_string = " " * spacing
        print(spacing_string + node.value)

        for i in node.children:
            self.print_node(i, spacing + 2)


