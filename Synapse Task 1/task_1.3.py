encoded_lists= [
    [1,2,3,4,6],
    [5,7,8,9,15],
    [12,14,16,18],
    [10,11,12,13,16,17,18,20]
]

def exploded_lists(lst):
    for inner_list in lst:
        i = 0
        while i < len(inner_list) - 2:
            if inner_list[i + 1] == inner_list[i] + 1 and inner_list[i + 2] == inner_list[i] + 2:
                inner_list.pop(i)
                inner_list.pop(i)
                inner_list.pop(i)
                
            else:
                i += 1

exploded_lists(encoded_lists)
print(encoded_lists)





