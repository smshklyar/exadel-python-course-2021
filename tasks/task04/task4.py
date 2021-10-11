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

al = []
def df(d):
    if isinstance(d, dict):
        for k, v in d.items():
            if isinstance(v, dict):
                df(v)
            else:
                for i in v:
                    al.append(i)
    else:
        for i in d:
            al.append(i)
    return (al)

def collect_leaves(tr):
    assert len(tr) != 0
    return df(tr)


print(collect_leaves(tree))
#print(collect_leaves([1, 3, 5]))
#print(collect_leaves([]))