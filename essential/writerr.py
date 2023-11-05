constant_pfile = "cont/admins"
import pickle
def writerr(constant):
    with open(constant_pfile, "wb") as w:
        pickle.dump(constant, w)

