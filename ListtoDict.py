name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

# def make_dict(arr1, arr2):
#     new_dict = {}
#     new_dict = dict(zip(arr1, arr2))
#     return new_dict


def make_dict(arr1, arr2):
    if len(arr1) >= len(arr2):
        keylist = arr1
        valuelist = arr2
    else:
        keylist = arr2
        valuelist = arr1
    for i in xrange(len(keylist)-len(valuelist)):
        valuelist.append("")
    new_dict = {}
    new_dict = dict(zip(keylist, valuelist))
    return new_dict

print make_dict(name, favorite_animal)
