import pickle
constant_pfile = "cont/dictionary"

def reader():
    with open(constant_pfile, "rb") as r:
        dic = pickle.load(r)
    return dic

