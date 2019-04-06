#!/usr/bin/env python2

import sys
import struct
from  struct import *
import binascii
import time

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

def new_image(name, extension, byte_arr):
  file_name = name + "." + extension
  print ("%s has been created" % file_name)
  image = open(file_name, "wb")
  image.write(byte_arr)

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

magic, version, timestamp  = struct.unpack("<LLL", data[0:12])
author = ''.join(struct.unpack("<8s", data[12:20]))
num_sections = struct.unpack("<L", data[20:24])
num_sections = int(num_sections[0])

if (num_sections <= 0):
  bork("Expected a positive number, got %d" % int(num_sections))

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))


print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % time.ctime(timestamp))
print("AUTHOR: %s" % str(author))
print("SECTIONS: %d" % int(num_sections))



# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

start = 24

for i in range(0, num_sections):
  stype, slen = struct.unpack("<LL", data[start:start+8])
  slen = int(slen)
 
  #print("Section: Num: %d Type: %s Length: %d" % (i, stype, slen))

  if stype == SECTION_ASCII:
    unpack_str = "<%ds" % slen
    output = ''.join(struct.unpack(unpack_str, data[start+8:(start+8+slen)]))
    print("ASCII Output: %s" % (output))

  elif stype == SECTION_UTF8:
    unpack_str = "<%ds" % slen
    output = ''.join(struct.unpack(unpack_str, data[start+8:(start+8+slen)]))
    output = output.decode('utf-8')
    print("UTF-8 Output: %s" % (output))
  
  elif stype == SECTION_WORDS:
    num_words = int(slen/4)
    unpack_str = "%s" % 'L'*num_words
    unpack_str = "<" + unpack_str
    output = ''.join(struct.unpack(unpack_str, data[start+8:(start+8+slen)]))
    print("Words Output: %s" % (output))

  elif stype == SECTION_COORD:
    if slen == 16:
      unpack_str = "<dd"
      coordinates = struct.unpack(unpack_str, data[start+8:(start+8+slen)])
      # Checking for valid coordinates
      x_coord = coordinates[0]
      y_coord = coordinates[1]

      if (x_coord > 180) or (x_coord < -180) or (y_coord > 180) or (y_coord < -180) :
        bork("Invalid coordinates")
      else :
        print("Coordinates Output: %s" % str(coordinates))
    else:
      bork("SECTION COORD Requires 16 bytes, only recieved %d" % slen)

  elif stype == SECTION_REFERENCE:
    if slen == 4:
      unpack_str = "<L"
      ref = struct.unpack(unpack_str, data[start+8:(start+8+slen)])
      ref = ref[0]
      print("Reference Output: %d" % ref)
    else:
      bork("Reference must have exactly 4 bytes, this has %d" % slen)
  elif stype == SECTION_PNG:
    unpack_str = "%s" % 'B'*(slen)
    unpack_str = "<" + unpack_str
    png_sig = [137, 80, 78, 71, 13, 10, 26, 10]
    png_data = struct.unpack(unpack_str, data[start+8:(start+8+slen)])

    png = png_sig + list(png_data)

    new_image("fpff-extracted-png", "png", bytearray(png))

  elif stype == SECTION_GIF87:
    unpack_str = "%s" % 'B'*(slen)
    unpack_str = "<" + unpack_str
    gif87_sig = [47, 49, 46, 38, 37, 61]
    gif87_data = struct.unpack(unpack_str, data[start+8:(start+8+slen)])

    gif87 = gif87_sig + list(png_data)

    new_image("fpff-extracted-gif87", "gif", bytearray(gif87))

  elif stype == SECTION_GIF89:
    unpack_str = "%s" % 'B'*(slen)
    unpack_str = "<" + unpack_str
    gif89_sig = [47, 49, 46, 38, 39, 61]
    gif89_data = struct.unpack(unpack_str, data[start+8:(start+8+slen)])

    gif89 = gif89_sig + list(png_data)
    new_image("fpff-extracted-gif89", "gif", bytearray(gif89))
    

  start = start + slen + 8



