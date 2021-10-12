tree = {
   "node1": {
       "node11": {
           "node111": [1, 2, 3],
           "node112": [31, 5]
       },
       "node12": [31]
   },
   "node2": [7, 8, 9]
}

def collect_leaves(lf):
    if isinstance(lf, dict):
        al = []
        for k in lf:
            al.extend(collect_leaves(lf[k]))
        return al
    else:
        return lf


assert collect_leaves(tree) == [1, 2, 3, 31, 5, 31, 7, 8, 9], "test error"
assert collect_leaves([1, 2, 3]) == [1, 2, 3], "test error"
print(collect_leaves(tree))