#Copyright (c) 2026 Benjamin Winter
#This file is part of BasicMemManip which is released under the MIT License.
#See file LICENSE or go to https://github.com/core2000-eU/BasicMemManip for full license details.

#DESCRIPTION
#BasicMemManip, a Python module that extends Python with some low-level, C/C++ -related features (intended to be used in combination with Pythons ctypes library)

#imports
import                              sys
import                              ctypes

def writeStrAtAddr(addr=0, value="", maxchar=-1, nullterminated=True, encoding="UTF-8"):
    """
    brief Write python String [value] to memory address [addr] in format of a C/C++ char
    param [addr] INT the address or a ctypes object that can be interpreted as an address
    param [value] STR The python STR to write
    param [maxchar] INT specify the num. of characters to write, by default the entire string will be written;
                    if nullterminated=True -> [maxchar] will be [maxchar] +1 to account for the nulltermination character (keep your buffer size in mind);
    param [nullterminated] BOOL
                    set TRUE if you want the additional nulltermination character [\x00] (keep buffer size in mind, needs 1 byte!);
                    set false if you don't want the nulltermination character
    param [encoding] STR set the encoding type; this parameter is used directly in the [string].encode() function; default: "UTF-8"
    returns [] None
    """
    try:
        #cut string to maxchar
        if(maxchar > -1):
            if(len(value) > maxchar): value = value[0:maxchar]
        #create temporary buffer that holds the content
        cobjtemp = ctypes.create_string_buffer(value.encode(encoding)); cobjtemp_addr = ctypes.addressof(cobjtemp); cobjtemp_sizeof = ctypes.sizeof(cobjtemp)
        #copy temporary string buffer to destination memory address
        if(nullterminated):     ctypes.memmove(addr, cobjtemp_addr, cobjtemp_sizeof)
        else:                   ctypes.memmove(addr, cobjtemp_addr, cobjtemp_sizeof-1)
        #make memory available to garbage collector
        del(cobjtemp); del(cobjtemp_addr); del(cobjtemp_sizeof)
    except Exception as e:
        exc_type, exc_object, exc_traceback = sys.exc_info(); exc_linenum = exc_traceback.tb_lineno
        raise Exception(f"writeStrAtAddr() raised Exception [{str(e)}] in line [{str(exc_linenum)}]")

def writeWStrAtAddr(addr=0, value="", maxchar=-1, nullterminated=True):
    """
    brief Write python String [value] to memory address [addr] in format of a C/C++ WSTR (16-bit wide string)
    param [addr] INT the address or a ctypes object that can be interpreted as an address
    param [value] STR The python STR to write
    param [maxchar] INT specify the num. of characters to write, by default the entire string will be written; [maxchar] will be [maxchar] +1 to account for the nulltermination character (keep your buffer size in mind)
    param [nullterminated] BOOL is always true and MUST NOT be modified. Strings in buffer are always nullterminated
    returns [] None
    """
    try:
        #cut string to maxchar
        if(maxchar > -1):
            if(len(value) > maxchar): value = value[0:maxchar]
        #create temporary buffer that holds the content
        cobjtemp = ctypes.create_unicode_buffer(value); cobjtemp_addr = ctypes.addressof(cobjtemp); cobjtemp_sizeof = ctypes.sizeof(cobjtemp)
        #copy temporary string buffer to destination memory address
        ctypes.memmove(addr, cobjtemp_addr, cobjtemp_sizeof)
        #make memory available to garbage collector
        del(cobjtemp); del(cobjtemp_addr); del(cobjtemp_sizeof)
    except Exception as e:
        exc_type, exc_object, exc_traceback = sys.exc_info(); exc_linenum = exc_traceback.tb_lineno
        raise Exception(f"writeWStrAtAddr() raised Exception [{str(e)}] in line [{str(exc_linenum)}]")

def writeULongAtAddr(addr=0, value=0):
    """
    brief Write python INT [value] to memory address [addr] in format of a C/C++ unsigned long
    param [addr] INT the address or a ctypes object that can be interpreted as an address
    param [value] INT The python INT to write
    returns [] None
    """
    try:
        #create temporary buffer that holds the content
        cobjtemp = ctypes.c_ulong(value); cobjtemp_addr = ctypes.addressof(cobjtemp); cobjtemp_sizeof = ctypes.sizeof(cobjtemp)
        #copy temporary string buffer to destination memory address
        ctypes.memmove(addr, cobjtemp_addr, cobjtemp_sizeof)
        #make memory available to garbage collector
        del(cobjtemp); del(cobjtemp_addr); del(cobjtemp_sizeof)
    except Exception as e:
        exc_type, exc_object, exc_traceback = sys.exc_info(); exc_linenum = exc_traceback.tb_lineno
        raise Exception(f"writeULongAtAddr() raised Exception [{str(e)}] in line [{str(exc_linenum)}]")
        
def readULongAtAddr(addr=0):
    """
    brief Read C/C++ unsigned long at memory address [addr] and return a Python int
    param [addr] INT the address or a ctypes object that can be interpreted as an address
    returns [value] INT
    """
    try:
        return int(ctypes.cast(addr, ctypes.POINTER(ctypes.c_ulong)).contents.value)
    except Exception as e:
        exc_type, exc_object, exc_traceback = sys.exc_info(); exc_linenum = exc_traceback.tb_lineno
        raise Exception(f"readULongAtAddr() raised Exception [{str(e)}] in line [{str(exc_linenum)}]")

def writeULongLongAtAddr(addr=0, value=0):
    """
    brief Write python INT [value] to memory address [addr] in format of a C/C++ unsigned long long
    param [addr] INT the address or a ctypes object that can be interpreted as an address
    param [value] INT The python INT to write
    returns [] None
    """
    try:
        #create temporary buffer that holds the content
        cobjtemp = ctypes.c_ulonglong(value); cobjtemp_addr = ctypes.addressof(cobjtemp); cobjtemp_sizeof = ctypes.sizeof(cobjtemp)
        #copy temporary string buffer to destination memory address
        ctypes.memmove(addr, cobjtemp_addr, cobjtemp_sizeof)
        #make memory available to garbage collector
        del(cobjtemp); del(cobjtemp_addr); del(cobjtemp_sizeof)
    except Exception as e:
        exc_type, exc_object, exc_traceback = sys.exc_info(); exc_linenum = exc_traceback.tb_lineno
        raise Exception(f"writeULongLongAtAddr() raised Exception [{str(e)}] in line [{str(exc_linenum)}]")
        
def readULongLongAtAddr(addr=0):
    """
    brief Read C/C++ unsigned long long at memory address [addr] and return a Python int
    param [addr] INT the address or a ctypes object that can be interpreted as an address
    returns [value] INT
    """
    try:
        return int(ctypes.cast(addr, ctypes.POINTER(ctypes.c_ulonglong)).contents.value)
    except Exception as e:
        exc_type, exc_object, exc_traceback = sys.exc_info(); exc_linenum = exc_traceback.tb_lineno
        raise Exception(f"readULongLongAtAddr() raised Exception [{str(e)}] in line [{str(exc_linenum)}]")

def writeBytesAtAddr(addr=0, value=[]):
    """
    brief Write bytes at memory address [addr]
    param [addr] INT the address or a ctypes object that can be interpreted as an address
    param [value] INT-type LIST (careful: NOT designed for a bytearray) containing the bytes to be written
    returns [] None
    """
    try:
        #cobjtemp = ctypes.cast(address, ctypes.POINTER(ctypes.c_ubyte*len(value))  )
        #cobjtemp.contents[0:len(value)] = value[0:len(value)]
        ctypes.cast(addr, ctypes.POINTER(ctypes.c_byte*len(value))  ).contents[0:len(value)] = value[0:len(value)]
    except Exception as e:
        exc_type, exc_object, exc_traceback = sys.exc_info(); exc_linenum = exc_traceback.tb_lineno
        raise Exception(f"writeBytesAtAddr() raised Exception [{str(e)}] in line [{str(exc_linenum)}]")

def readBytesAtAddr(addr=0, count=1):
    """
    brief Reads [count] number of bytes at memory address [addr] and returns them as a Python INT-type LIST
    param [addr] INT the address or a ctypes object that can be interpreted as an address
    param [count] INT number of bytes to read; default:1
    returns [value] INT-type LIST (or actually, to be precise, a ctypes c_byte_Array type which you ran read from like a default python INT-type LIST)
    """
    try:
        return ctypes.cast(addr, ctypes.POINTER(ctypes.c_byte*count)).contents[0:count]
    except Exception as e:
        exc_type, exc_object, exc_traceback = sys.exc_info(); exc_linenum = exc_traceback.tb_lineno
        raise Exception(f"readBytesAtAddr() raised Exception [{str(e)}] in line [{str(exc_linenum)}]")

def writeUBytesAtAddr(addr=0, value=[]):
    """
    brief Write unsigned bytes at memory address [addr]
    param [addr] INT the address or a ctypes object that can be interpreted as an address
    param [value] INT-type LIST (careful: NOT designed for a bytearray) containing the bytes to be written
    returns [] None
    """
    try:
        ctypes.cast(addr, ctypes.POINTER(ctypes.c_ubyte*len(value))  ).contents[0:len(value)] = value[0:len(value)]
    except Exception as e:
        exc_type, exc_object, exc_traceback = sys.exc_info(); exc_linenum = exc_traceback.tb_lineno
        raise Exception(f"writeUBytesAtAddr() raised Exception [{str(e)}] in line [{str(exc_linenum)}]")

def readUBytesAtAddr(addr=0, count=1):
    """
    brief Reads [count] number of unsigned bytes at memory address [addr] and returns them as a Python INT-type LIST
    param [addr] INT the address or a ctypes object that can be interpreted as an address
    param [count] INT number of bytes to read; default:1
    returns [value] INT-type LIST (or actually, to be precise, a ctypes c_ubyte_Array type which you ran read from like a default python INT-type LIST)
    """
    try:
        return ctypes.cast(addr, ctypes.POINTER(ctypes.c_ubyte*count)).contents[0:count]
    except Exception as e:
        exc_type, exc_object, exc_traceback = sys.exc_info(); exc_linenum = exc_traceback.tb_lineno
        raise Exception(f"readUBytesAtAddr() raised Exception [{str(e)}] in line [{str(exc_linenum)}]")

def allocateNBytes(size,zero=True):
    """
    brief Allocate [size] number of bytes in memory (coherent). you can free() the allocated memory by deleting all references to [object] that is returned (GarbageCollector will do the work for you)
    param [size] INT the size, in bytes, to allocate
    param [zero] BOOL zero the allocated memory after allocation; typically not neccessary but ensures fully-zeroed block; set False to enhance speed; default:True
    returns [object] ctypes.create_string_buffer() object
    returns [addr] INT address of the allocated buffer
    """
    try:
        #allocate buffer
        c_newalloc = ctypes.create_string_buffer(size)
        c_newalloc_addr = ctypes.addressof(c_newalloc)
        #zero
        if(zero): ctypes.memset(c_newalloc_addr, 0, size)
        #return
        return c_newalloc, c_newalloc_addr
    except Exception as e:
        exc_type, exc_object, exc_traceback = sys.exc_info(); exc_linenum = exc_traceback.tb_lineno
        raise Exception(f"allocateNBytes() raised Exception [{str(e)}] in line [{str(exc_linenum)}]")
        
def writechar_p_array(value=[], encoding="UTF-8"):
    """
    brief NOT FOR PRODUCTIVE USE
            ctypes library supports [c_char_p] now, so don't use this implementation. It's unneccessary and untested.
            allocate memory and write an array of c_char_p; useful for C/C++ argv; note that this represents char argv[], NOT char *argv[]
    param [value] LIST a LIST containing the STRs that will be written to memory
    param [encoding] STR set the encoding type; this parameter is used directly in the encode() function; default: "UTF-8"
    returns [addr] INT the address of the first array entry; the array is nullterminated
    returns [objects_to_keep] LIST a LIST of objects you should always keep a reference to, or all data in memory WILL BE REMOVED
    """
    try:
        objects_to_keep = []
        #array itself
        size_of_pointer = ctypes.sizeof(ctypes.c_void_p) #calculate size of a pointer, will return 8 bytes on 64-bit
        size_of_arraybuffer = ((size_of_pointer)*len(value)) + size_of_pointer #one pointer per entry, plus nulltermination
        objects_to_keep.append( allocateNBytes(size=size_of_arraybuffer) )
        #c_char_p's and array entries
        array_addr_current = int(objects_to_keep[-1][1]); #current address we're working on within the array
        for i in value:
            #c_char_p's:
            objects_to_keep.append( allocateNBytes(size=len(i)+1) ) #1 byte per character + nulltermination character
            writeStrAtAddr( addr=objects_to_keep[-1][1], value=i, nullterminated=True, encoding=encoding )
            #array entries:
            if(ctypes.sizeof(ctypes.c_void_p) == 4):    writeULongAtAddr(addr=array_addr_current, value=objects_to_keep[-1][1])
            elif(ctypes.sizeof(ctypes.c_void_p) == 8):  writeULongLongAtAddr(addr=array_addr_current, value=objects_to_keep[-1][1])
            else:                                       raise Exception(f"unknown architecture, 32-bit and 64-bit only at this time")
            array_addr_current += size_of_pointer
        #last entry in array should already be zeroed out to make array nullterminated
        return int(objects_to_keep[0][1]), objects_to_keep
    except Exception as e:
        exc_type, exc_object, exc_traceback = sys.exc_info(); exc_linenum = exc_traceback.tb_lineno
        raise Exception(f"writechar_p_array() raised Exception [{str(e)}] in line [{str(exc_linenum)}]")
        
def readchar_p_array(addr=0):
    """
    brief NOT FOR PRODUCTIVE USE
            ctypes library supports [c_char_p] now, so don't use this implementation. It's unneccessary and untested.
            brief read array of c_char_p; useful for C/C++ argv; note that this represents char argv[], NOT char *argv[]
    param [addr] INT the address of the char argv[] (address of the first array entry)
    returns []
    """
    try:
        pass;
    except Exception as e:
        exc_type, exc_object, exc_traceback = sys.exc_info(); exc_linenum = exc_traceback.tb_lineno
        raise Exception(f"readchar_p_array() raised Exception [{str(e)}] in line [{str(exc_linenum)}]")
