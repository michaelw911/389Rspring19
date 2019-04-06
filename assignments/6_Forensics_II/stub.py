#!/usr/bin/env python2

import sys
import struct
from  struct import *
import binascii
import time

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1
TIMESTAMP = 0 #need to change

SECTION_ASCII = 1
SECTION_UTF8 = 2
SECTION_WORDS = 3
SECTION_DWORDS = 4
SECTION_DOUBLES = 5
SECTION_COORD = 6
SECTION_REFERENCE = 7
SECTION_PNG = 8
SECTION_GIF87 = 9
SECTION_GIF89 = 10


if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8

magic, version, timestamp, author = struct.unpack("<LLLQ", data[0:20])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))


print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % time.ctime(timestamp))
print("AUTHOR: %s" % reverse(str(hex(author)[2:]).decode("hex")))


# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")


start = 20
end = 28

line = 1
while line:
  #time.sleep(1)
  try:
    stype, slen = struct.unpack("<LL", data[start:end])
    print stype
    print len(data)
    #slen, stype = struct.unpack("<LL", data[start:end])
    print ("Stype %s %d " % (hex(stype), int(stype)))
    #print ("dlen %s  %d" % (hex(slen), int(slen)))
    #print ("Stype %s slen %s" % (hex(stype), hex(slen)))

  #except: 
    #bork("End of input")
  finally:
    #start = start + 1 
    #end = end + 1 

    if stype == SECTION_ASCII:
      #slen = 0
      #while (slen == 0):
       # slen, gar = struct.unpack("<BB", data[start:end+1])
       # start = start + 1 
       # end = end + 1 
      
      print ("ASCII header: SLEN bytes %d " % (int(slen)))

      print sys.getsizeof(slen)
      print sys.getsizeof(stype)

      total = sys.getsizeof(slen) + sys.getsizeof(stype) + int(slen)
      print("total size %d" % total)
      output =""
      start = end-1
      for i in range(0, int(slen)):
        start = start  +1
        loc_end = start + 1
        char = struct.unpack("<B", data[start:loc_end])

        char = char[0]

        print ("Ascii Stype %s %d %c" % (format(char, 'x'), int(char), chr(char)))
        output = output + chr(char)
        #start = start + 1
        #$end = end + 1
     
      print output
      time.sleep(1)
      start = loc_end
      end = loc_end + 8

      print start
      print end


    elif stype == SECTION_UTF8:
      print ("utf8 header: SLEN bytes %d")
      start = start + 4
      end = end + 4


    elif stype  == SECTION_WORDS:
      print ("words header: SLEN bytes %d")
    elif stype  == SECTION_DWORDS:
      print ("dwords header: SLEN bytes %d")
    elif stype  == SECTION_DOUBLES:
      print ("doubles header: SLEN bytes %d" % int(slen))
      start = start + 4
      end = end + 4
    elif stype  == SECTION_COORD:
      print ("coord header: SLEN bytes %d"  % (int(slen)))

      start = end
      loc_end = start + 16
      x, y = struct.unpack("<QQ", data[start:loc_end])
      time.sleep(1)
      
      output = (x,y)


      print output
      time.sleep(1)

      start = loc_end
      end = loc_end + 8


    elif stype  == SECTION_REFERENCE:
      print ("reference header: SLEN bytes %d")
    elif stype  == SECTION_PNG:
      
      start = end - 1

      print ("png header: SLEN bytes %d" % (int(slen)))
      time.sleep(1)
      png = "89  50  4e  47  0d  0a  1a  0a"
      for i in range(0, int(slen)-8):
        
       # time.sleep(1)
        start = start + 1
        loc_end = start + 1
        try :
          char = struct.unpack("<B", data[start:loc_end])
          char = char[0]
        finally:

          print ("Byte %d png Stype %s %d " % (int(i), hex(char), int(char)))
          print ("Start %d End %d" % (start, loc_end))
          png = png + " " + format(char, 'x')


      print png
      time.sleep(1)


    elif stype  == SECTION_GIF87:
      print ("gif87 header: SLEN bytes %d")
    elif stype  == SECTION_GIF89:
      print ("gif89 header: SLEN bytes %d")
    else :
      start = start + 4
      end = end + 4
