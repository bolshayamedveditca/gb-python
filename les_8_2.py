def huffman_tree(frequency):
    size = len(frequency)
    nodes = [Node(char, frequency.get(char)) for char in frequency.keys()]
    for _ in range(size - 1):
        nodes.sort(key=lambda n: n.weight)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node('', left.weight + right.weight)
        parent.left = left
        parent.right = right
        nodes.append(parent)
    return nodes.pop()

def left_right(node, c):
    if node.left and node.left.value == c:
        return '0'
    if node.right and node.right.value == c:
        return '1'
    if node.left:
        d = left_right(node.left, c)
        if d is not None:
            return '0'+d
    if node.right:
        e = left_right(node.right, c)
        if e is not None:
            return '1'+e
    return None

s = input()

class Node:
    def __init__(self, a, b):
        self.value = a
        self.weight = b
        self.left = None
        self.right = None

dicti = {}
dicti2 = {}

for i in s:
    dicti[i] = s.count(i)

spam = huffman_tree(dicti)

for i in dicti.keys():
    dicti2[i] = left_right(spam, i)

result = ''
for i in s:
    result += dicti2[i]

print(result)

