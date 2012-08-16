from ctypes import cdll, c_int32, c_void_p, c_char_p, create_string_buffer
from ctypes.util import find_library

libCarbon = cdll.LoadLibrary(find_library("CoreFoundation.framework"))
libCarbon.CFStringCreateWithCString.argtypes = [ c_void_p, c_char_p, c_int32 ]
libCarbon.CFStringCreateWithCString.restype = c_void_p
libCarbon.CFStringGetLength.argtypes = [ c_void_p ]
libCarbon.CFStringGetLength.restype = c_int32
libCarbon.CFStringGetCString.argtypes = [ c_void_p, c_char_p, c_int32, c_int32 ]
libCarbon.CFStringGetCString.restype = c_int32
libCarbon.CFRelease.argtypes = [ c_void_p ]
libCarbon.CFRelease.restype = None
    
def create_cfstringref(str):
    return libCarbon.CFStringCreateWithCString(0, str, 0)
    
def release_cfstringref(cfstringref):
    _ = libCarbon.CFRelease(cfstringref)
    return None
    
def str_from_cfstringref(cfstringref):
    length = libCarbon.CFStringGetLength(cfstringref) + 1
    buff = create_string_buffer(length)
    libCarbon.CFStringGetCString(cfstringref, buff, length, 0)
    return buff.value
