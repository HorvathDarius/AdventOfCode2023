from math import gcd

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

starting_nodes = []

for node in nodes:
    if node.name[2] == 'A':
        starting_nodes.append(node)

# THIS ALGORITHM EVEN IF IT IS CORRECT
# IT IS A BRUTE FORCE APPROACH TO THIS PROBLEM
# THIS WOULD TAKE VERY LONG TO COMPLETE
"""
instructions_executed = 0
zzz_found = False
while not zzz_found:
    for instr in instructions:
        child_nodes = []
        if instr == 'L':
            for node in starting_nodes:
                node = node.left
                child_nodes.append(node)
        elif instr == "R":
            for node in starting_nodes:
                node = node.right
                child_nodes.append(node)

        instructions_executed += 1
        print(instructions_executed)
        starting_nodes = child_nodes
        all_true = True
        for node in starting_nodes:
            if node.name[2] != 'Z':
                all_true = False
        if all_true:
            zzz_found = True

print(instructions_executed)
"""
# TO SOLVE THIS PROBLEM WE MUST NOTICE THAT THE NODES THAT END WITH Z
# OCCUR IN A CERTAIN INTERVAL
# TO SOLVE THE PROBLEM WE CAN FIGURE OUT THE INTERVAL
loops = []
for current in starting_nodes:
    loop = []
    instructions_executed = 0
    z_found = False
    first_goal = True
    first_found = None

    while not z_found:
        for instr in instructions:
            if instr == 'L':
                current = current.left
            elif instr == "R":
                current = current.right
            instructions_executed += 1

            if current.name[2] == "Z":
                loop.append(instructions_executed)
                if first_goal:
                    first_found = current.name
                    first_goal = False
                    continue
                if first_found == current.name:
                    z_found = True
                    loops.append(loop)
                    break

# AND THEN FIND THE LEAST COMMON MULTIPLIER OF THOSE INTERVALS
loops = [loop[0] for loop in loops]
# least common multiplier
lcm = 1
for i in loops:
    lcm = lcm * i//gcd(lcm, i)
print(lcm)
