import pickle

with open("cont/qurand", "rb") as r:
    quran = pickle.load(r)
countrf = (len(quran) - 1)

