import ctypes
import os



lib = ctypes.CDLL(os.path.abspath("./libasm.so"))
lib.add.argtypes = [ctypes.c_long,ctypes.c_long]
lib.add.restype = ctypes.c_long

def add(a,b):
    return lib.add(a,b)