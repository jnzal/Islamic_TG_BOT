import pickle

pfile = 'cont/admins'
def readerr():
    di = 1
    with open(pfile, "rb") as r:
         di = pickle.load(r)
    return di

