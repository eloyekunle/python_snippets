from itertools import combinations
def get_pairs_from_set(node_set):
    return list(combinations(node_set, 2))

class Tree:
    def __init__(self):
        self.root = None
        self.inserted = {}

    def __len__(self):
        return len(self.inserted)

    def create(self, node1_data, node2_data):
        node1 = Node(node1_data)
        node2 = Node(node2_data)
        if self.root is None:
            self.root = node1
            self.root.level = 1
            self.inserted[self.root.data] = self.root

        not_inserted = {node1, node2} - set(self.inserted.values())
        inserted = self.inserted[list({node1,node2} - not_inserted)[0].data]
        not_inserted_node = list(not_inserted)[0]
        not_inserted_node.level = inserted.level + 1
        not_inserted_node.parent = inserted.data
        inserted.children[not_inserted_node.data] = not_inserted_node
        self.inserted[not_inserted_node.data] = inserted.children[not_inserted_node.data]

class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.level = 0
        self.parent = None

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return hash(self.data)

def calc_distance(v1, v2):
    v1_node = inserted[v1]
    v2_node = inserted[v2]

    parents_1 = set()
    parent_1 = v1_node.data
    while parent_1 is not None:
        parents_1.add(inserted[parent_1])
        parent_1 = inserted[parent_1].parent

    parents_2 = set()
    parent_2 = v2_node.data
    while parent_2 is not None:
        parents_2.add(inserted[parent_2])
        parent_2 = inserted[parent_2].parent

    len_common_parents = len(parents_1 & parents_2)
    return (v1_node.level - len_common_parents) + (v2_node.level - len_common_parents)

def kittyCalc(set_pairs):
    pairs = get_pairs_from_set(set_pairs)
    print(pairs)
    kitty = 0
    for n,m in pairs:
        kitty += (n*m*calc_distance(n,m))
        kitty %= (10**9 + 7)
    return kitty

if __name__ == '__main__':
    n,q = list(map(int, input().split()))
    t = Tree()
    for _ in range(n-1):
        pair = list(map(int, input().split()))
        t.create(*pair)
    inserted = t.inserted
    for i in range(q):
        _ = input()
        k_set = set(map(int, input().split()))
        print(i, kittyCalc(k_set))
#
# if __name__ == '__main__':
#     nodes = [[1,2], [3,1], [4,1], [3,5], [3,6], [3,7]]
#     t = Tree()
#     for x,y in nodes:
#         t.create(x,y)
#     inserted = t.inserted
#     assert kittyCalc(t.root, {2,4}) == 16
#     assert kittyCalc(t.root, {2,1}) == 2
#     assert kittyCalc(t.root, {5}) == 0
#     assert kittyCalc(t.root, {2,4,5}) == 106