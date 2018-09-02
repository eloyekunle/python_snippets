from itertools import combinations
def get_pairs_from_set(node_set):
    return list(combinations(node_set, 2))

class Tree:
    def __init__(self):
        self.root = None

    def create(self, conn_node_data, data):
        conn_node = Node(conn_node_data)
        if self.root is None:
            self.root = conn_node
            self.root.level = 1

        current = self.root
        new_node = Node(data)
        def insert(current):
            if current == conn_node:
                new_node.level = current.level + 1
                current.children[data] = new_node
            else:
                for k,v in current.children.items():
                    insert(v)

        insert(current)

class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.level = 0

    def __eq__(self, other):
        return self.data == other.data

def calc_distance(root, v1, v2):
    global found
    global count
    global lev_sum
    count = 0
    found = []
    lev_sum = 0
    def lca(root_node):
        global found
        global count
        global lev_sum
        temp = None
        if root_node is None:
            return None
        if root_node.data in (v1, v2):
            return root_node

        for child in root_node.children.values():
            result = lca(child)
            if result and result not in found and count < 2:
                count += 1
                found.append(result)
                lev_sum += result.level
                temp = result

        if count == 2:
            return root_node

        return temp

    k_lca = lca(root).level
    return lev_sum - (2 * k_lca)

def kittyCalc(root, set_pairs):
    pairs = get_pairs_from_set(set_pairs)
    kitty = 0
    for n,m in pairs:
        kitty += (n*m*calc_distance(root,n,m))
        kitty %= (10**9 + 7)
    return kitty

if __name__ == '__main__':
    nodes = [[1,2], [1,3], [1,4], [3,5], [3,6], [3,7]]
    t = Tree()
    for x,y in nodes:
        t.create(x,y)
    assert kittyCalc(t.root, {2,4}) == 16
    assert kittyCalc(t.root, {5}) == 0
    assert kittyCalc(t.root, {2,4,5}) == 106