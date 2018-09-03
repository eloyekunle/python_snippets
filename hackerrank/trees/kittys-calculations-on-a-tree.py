from itertools import combinations
from collections import defaultdict

def get_pairs_from_set(node_set):
    return list(combinations(sorted(node_set), 2))

class Tree:
    def __init__(self):
        self.root = None
        self.inserted = {}
        self.distances = defaultdict(lambda: defaultdict(int))

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
        parent = self.inserted[list({node1,node2} - not_inserted)[0].data]
        not_inserted_node = list(not_inserted)[0]
        not_inserted_node.level = parent.level + 1
        not_inserted_node.parent = parent.data
        parent.children[not_inserted_node.data] = not_inserted_node
        self.inserted[not_inserted_node.data] = parent.children[not_inserted_node.data]
        while parent:
            for sibling in parent.children.keys():
                self.distances[sibling][not_inserted_node.data] = self.distances[not_inserted_node.data][sibling] = not_inserted_node.level - parent.level + 1
            if parent.parent is None:
                self.distances[parent.data][not_inserted_node.data] = self.distances[not_inserted_node.data][parent.data] = not_inserted_node.level - parent.level
                break
            parent = self.inserted[parent.parent]

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
    if distances[v1][v2]:
        return distances[v1][v2]
    elif distances[v2][v1]:
        return distances[v2][v1]
    else:
        distance = calc_distance(v1_node.parent, v2_node.parent) + 2
        distances[v1][v2] = distances[v2][v1] = distance
        return distance

def kittyCalc(set_pairs):
    pairs = get_pairs_from_set(set_pairs)
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
    distances = t.distances
    for i in range(q):
        _ = input()
        k_set = set(map(int, input().split()))
        print(kittyCalc(k_set))

# if __name__ == '__main__':
#     nodes = [[1,2], [3,1], [4,1], [3,5], [3,6], [3,7]]
#     t = Tree()
#     for x,y in nodes:
#         t.create(x,y)
#     inserted = t.inserted
#     distances = t.distances
#     assert kittyCalc({2,4}) == 16
#     assert kittyCalc({2,1}) == 2
#     assert kittyCalc({5}) == 0
#     assert kittyCalc({2,4,5}) == 106