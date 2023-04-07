
"""
Created the 04/04/2023

@author: Sebastien Weber
"""
import sys
from ctypes import CFUNCTYPE

if 'win32' in sys.platform:
    from ctypes import WINFUNCTYPE


def winfunc(name, dll, result, *args):
    """build and apply a ctypes prototype complete with parameter flags
    Parameters
    ----------
    name:(str) function name in the dll
    dll: (ctypes.windll) dll object
    result: result is the type of the result (c_int,..., python function handle,...)
    args: list of tuples with 3 or 4 elements each like (argname, argtype, in/out, default) where argname is the
    name of the argument, argtype is the type, in/out is 1 for input and 2 for output, and default is an optional
    default value.

    Returns
    -------
    python function
    """
    atypes = []
    aflags = []
    for arg in args:
        atypes.append(arg[1])
        aflags.append((arg[2], arg[0]) + arg[3:])
    return WINFUNCTYPE(result, *atypes)((name, dll), tuple(aflags))


def cfunc(name, dll, result, *args):
    """build and apply a ctypes prototype complete with parameter flags

    Parameters
    ----------
    name: (str) function name in the dll
    dll: (ctypes.windll) dll object
    result : result is the type of the result (c_int,..., python function handle,...)
    args: list of tuples with 3 or 4 elements each like (argname, argtype, in/out, default) where argname is the
    name of the argument, argtype is the type, in/out is 1 for input and 2 for output, and default is an optional
    default value.

    Returns
    -------
    python function
    """
    atypes = []
    aflags = []
    for arg in args:
        atypes.append(arg[1])
        aflags.append((arg[2], arg[0]) + arg[3:])
    return CFUNCTYPE(result, *atypes)((name, dll), tuple(aflags))