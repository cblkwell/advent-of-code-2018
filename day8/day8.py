from sys import argv

inputfile = argv[1]

def construct_tree(license):
    children = license.pop(0)
    md_entries = license.pop(0)
    subnodes = 0
    tree = [ children, md_entries ]
    child_nodes = []

# Represent each node as a list with this structure:
# [ children, md_entries, md_values (list), child_nodes (list) ]

    while subnodes < children:
        node, license = construct_tree(license)
        child_nodes.append(node)
        subnodes += 1

    md_values = []
    for count in range(0, md_entries):
        md_values.append(license.pop(0))

    tree.append(md_values)
    tree.append(child_nodes)

    return tree, license

    
def sum_metadata(tree):
    total = 0
    for md_value in tree[2]:
        total = total + md_value

    for node in tree[3]:
        total = total + sum_metadata(node)
 
    return total


def sum_node(node):
    value = 0
    md_values = node[2]
    child_nodes = node[3]

    if node[0] == 0:
        value = sum(md_values)
    else:
        for child in md_values: 
            try:
                child_value = sum_node(child_nodes[child - 1])
            except:
                child_value = 0

            value = value + child_value

    return value


with open(inputfile) as file:
    license = file.read().rstrip().split()
    license = list(map(int, license))

tree = construct_tree(license)
print(sum_metadata(tree[0]))
print(sum_node(tree[0]))
