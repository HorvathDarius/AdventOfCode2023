lines = open('Day8-HauntedWasteland.txt').read().split('\n')

instructions = lines[0]
tree = lines[2:]


class Node:
    def __init__(self, name, left_child, right_child):
        self.name = name
        self.left = left_child
        self.right = right_child


def check_if_existing(name, nodes_arr):
    for existing in nodes_arr:
        if existing.name == name:
            return existing
    return None


nodes = []

for node in tree:
    root, children = node.split('=')
    root = root.strip()
    children = children.strip()
    left, right = children[1:-1].split(", ")
    if check_if_existing(root, nodes) is None:
        left_child = check_if_existing(left, nodes)
        if left_child is None:
            left_child = Node(left, None, None)
        nodes.append(left_child)
        right_child = check_if_existing(right, nodes)
        if right_child is None:
            right_child = Node(right, None, None)
        nodes.append(right_child)
        root = Node(root, left_child, right_child)
        nodes.append(root)
        nodes.append(left_child)
    else:
        existing = check_if_existing(root, nodes)

        left_child = check_if_existing(left, nodes)
        if left_child is None:
            left_child = Node(left, None, None)
        nodes.append(left_child)
        right_child = check_if_existing(right, nodes)
        if right_child is None:
            right_child = Node(right, None, None)
        nodes.append(right_child)
        existing.left = left_child
        existing.right = right_child

print("TREE CREATED")

root = check_if_existing("AAA", nodes)
original_instructions = instructions
instructions_executed = 0
zzz_found = False
iter = 0
while not zzz_found:
    for instr in instructions:
        if root.name == "ZZZ":
            zzz_found = True
            break
        if instr == 'L':
            root = root.left
            instructions_executed += 1
        elif instr == "R":
            root = root.right
            instructions_executed += 1
    print(f"ITERATION - {iter}")
    iter += 1
print(instructions_executed)

