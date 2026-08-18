#Copyright (c) 2026 Benjamin Winter
#This file is part of BasicMemManip which is released under the MIT License.
#See file LICENSE.TXT or go to https://github.com/core2000-eU/BasicMemManip for full license details.

#DESCRIPTION
#sample1.py for BasicMemManip, a Python module that extends Python with some low-level, C/C++ -related features (intended to be used in combination with Pythons ctypes library)

#imports
import                              time
import                              ctypes
import                              BasicMemManip

#global VARs
MemoryBuffer_obj =                  None
MemoryBuffer_address =              None

'''
ALLOCATING MEMORY AND INT-LIKE DATA TYPES
first, allocate 1000 (coherent) bytes in memory.
allocateNBytes() returns the RAW ctypes object (MemoryBuffer_obj) and the address (MemoryBuffer_address);
CAREFUL: you MUST store a reference to MemoryBuffer_obj during runtime. If you loose all references to it, python garbage collector will immediately free the allocated memory.
So, during runtime, make sure not to delete MemoryBuffer_obj.
See the end of this document to learn how to free() the allocated memory.
'''
MemoryBuffer_obj, MemoryBuffer_address = BasicMemManip.allocateNBytes(size=1000)

#store a C/C++ 64-bit unsigned long in the allocated memory. 4294967295 is the maximum decimal value before the unsigned long will overflow.
BasicMemManip.writeULongAtAddr(addr=MemoryBuffer_address, value=4294967295)

#next, read the unsigned long from memory:
print(f"value_ULong:            {BasicMemManip.readULongAtAddr(addr=MemoryBuffer_address)}")

#zero the allocated memory
ctypes.memset(MemoryBuffer_address, 0, 1000)

#store a C/C++ 64-bit unsigned long long in the allocated memory. 18446744073709551615 is the maximum decimal value before the unsigned long long will overflow.
BasicMemManip.writeULongLongAtAddr(addr=MemoryBuffer_address, value=18446744073709551615)

#next, read the unsigned long long from memory:
print(f"value_ULongLong:        {BasicMemManip.readULongLongAtAddr(addr=MemoryBuffer_address)}")

#zero memory
ctypes.memset(MemoryBuffer_address, 0, 1000)

'''
BYTES
Note that the library provides the following functions for Bytes:
for signed Bytes:       readBytesAtAddr()   /   writeBytesAtAddr()
for unsigned Bytes:     readUBytesAtAddr()  /   writeUBytesAtAddr()
'''
#next, we'll write multiple unsigned bytes to our allocated memory by using a python INT-type LIST:
BytesToWrite = [10, 11, 254, 255, 11, 10]
BasicMemManip.writeUBytesAtAddr(addr=MemoryBuffer_address, value=BytesToWrite)

#read the bytearray stored in memory. readUBytesAtAddr() returns them as a python INT-type LIST:
print(f"value_bytearray:        {BasicMemManip.readUBytesAtAddr(addr=MemoryBuffer_address, count=6)}")

#zero memory
ctypes.memset(MemoryBuffer_address, 0, 1000)

'''
STR
'''
#write STR (string) to allocated memory:
StringToWrite = "...HelloWorld...This is a STR... s t o r e d  n u l l - t e r m i n a t e d..."
BasicMemManip.writeStrAtAddr(addr=MemoryBuffer_address, value=StringToWrite)

#read the STR from memory, ctypes provides that directly:
print(f"value_STR:              {ctypes.string_at(MemoryBuffer_address)}")

#zero memory
ctypes.memset(MemoryBuffer_address, 0, 1000)

'''
WSTR
we can also write C++ WSTR to allocated memory. WSTRs are "wide strings", 2 bytes per character. They are used e.g. in Win SecurityDescriptors.
note that WSTRs are ALWAYS stored null-terminated, the nulltermination character takes up 2 bytes (1 full character) -> keep allocated memory size in mind!
'''
StringToWrite = "...HelloWorld...This is a WSTR... s t o r e d  n u l l - t e r m i n a t e d..."
BasicMemManip.writeWStrAtAddr(addr=MemoryBuffer_address, value=StringToWrite)

'''
ctypes memmove()
next, we allocate a second block of memory (coherent), and copy the contents from memory buffer 1 (used until now) to buffer 2 (new).
We then read both allocated memory blocks (which will show 1:1 the same content) and zero them out.
'''
#allocate new block of memory (coherent)
MemoryBuffer2_obj, MemoryBuffer2_address = BasicMemManip.allocateNBytes(size=1000)
#copy
ctypes.memmove(MemoryBuffer2_address, MemoryBuffer_address, 1000)
#read the WSTR from memory, ctypes provides that directly:
print(f"value_WSTR (block 1):   {ctypes.wstring_at(MemoryBuffer_address)}")
print(f"value_WSTR (block 2):   {ctypes.wstring_at(MemoryBuffer2_address)}")
#zero memory
ctypes.memset(MemoryBuffer_address, 0, 1000)
ctypes.memset(MemoryBuffer2_address, 0, 1000)


'''
FREE()
the only way to free() the allocated memory is to delete all references to MemoryBuffer_obj (which we created when calling allocateNBytes() at the beginning of this example).
python garbage collector will then free the memory for you:
'''
del(MemoryBuffer_obj); del(MemoryBuffer_address)
del(MemoryBuffer2_obj); del(MemoryBuffer2_address)

'''
showcase by allocating 250MB of memory, waiting 5 seconds, then free() ing that memory.
in taskmanager (or equivalent), you should see a spike in memory for ~5 seconds. The spike could show less than 250MB due to modern python/OS memory management.
'''
MemoryBuffer_obj, MemoryBuffer_address = BasicMemManip.allocateNBytes(size=250_000_000)
time.sleep(5)
del(MemoryBuffer_obj); del(MemoryBuffer_address)

#sleep 5 seconds to show that memory was actually free() during runtime and not on program exit:
time.sleep(5)

#upon exit of this program, the allocated memory would automatically be free()
