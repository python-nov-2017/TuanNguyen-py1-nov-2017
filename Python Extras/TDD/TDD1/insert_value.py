def insert_val_at(index, my_list, value):
    temp = list(my_list)
    if index > len(temp):
        return False
    temp.insert(index, value)
    return temp

