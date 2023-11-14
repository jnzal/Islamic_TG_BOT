constant_pfile = "cont/dictionary"
from time import sleep
import pickle
def writer(constant):
    with open(constant_pfile, "wb") as w:
        pickle.dump(constant, w)
    sleep(1)

