import os

from ._lib import lib, ffi

def _check_error(errno):
    if errno != 0:
        raise OSError(errno, os.strerror(errno))

def unshare(flags):
    res = lib.unshare(flags)
    if res != 0:
        _check_error(ffi.errno)


def setns(fd, flags):
    res = lib.setns(fd, flags)
    if res != 0:
        _check_error(ffi.errno)
        

for var in dir(lib):
    if var.startswith('CLONE_'):
        globals()[var] = getattr(lib, var)
