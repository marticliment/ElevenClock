#
#
#
#      File modified from https://github.com/ionescu007/wnfun
#
#      Some parts have been removed because they were useless in the context this script is intended
#      Additionally, the script has been optimized
#
#      All rights reserved to Alex Ionescu. 
#      See the license here: https://github.com/ionescu007/wnfun/blob/master/LICENSE
#
#


"""

Copyright (c) 2018 Gabrielle Viala. All Rights Reserved.
https://blog.quarkslab.com/author/gwaby.html

"""
import ctypes

ZwQueryWnfStateData = ctypes.windll.ntdll.ZwQueryWnfStateData

changeStamp = ctypes.c_ulong(0)
dataBuffer = ctypes.create_string_buffer(4096)
bufferSize = ctypes.c_ulong(ctypes.sizeof(dataBuffer))
nullBfr = ctypes.c_ulong(0)

def ReadWnfData(StateName):
    global bufferSize, changeStamp, dataBuffer
    StateName = ctypes.c_longlong(StateName)
    res = ZwQueryWnfStateData(ctypes.byref(StateName), 
        0, 0, 
        ctypes.byref(changeStamp), 
        ctypes.byref(dataBuffer), 
        ctypes.byref(bufferSize)
    )
    readAccess = 0 if res !=0 else 1
    bufferSize = nullBfr if res !=0 else bufferSize
    return readAccess, changeStamp.value, dataBuffer, bufferSize.value



def DoRead(StateName) -> bytes:
    _, _, dataBuffer, bufferSize = ReadWnfData(int(StateName, 16))
    return dataBuffer.raw[0:bufferSize]
    

#
#   End of https://github.com/ionescu007/wnfun code 
#
#
#   The following parts are simple definitions
#
#

def isFocusAssistEnabled() -> bool:
    try:
        return not DoRead("0xd83063ea3bf1c75") == b'\x00\x00\x00\x00'
    except Exception as e:
        print(e)
        return False


def getNotificationNumber() -> int:
    try:
        res = DoRead("0xd83063ea3bc1035")[0]
        assert type(res) == int, "Invalid value for notification number"
        return int(res)
    except Exception as e:
        print(e)
        return 0
