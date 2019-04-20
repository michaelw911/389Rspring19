#!/usr/bin/env python3

import hashlib
import string

def crack():
  hashes = open("../hashes.txt", "r").readlines()
 
  passwords = open("../passwords.txt", "r").readlines()
  characters = string.ascii_lowercase
    
  for c in characters:     
    for p in passwords:
      wd = c+p.rstrip()
      new_hash = hashlib.sha256(wd).hexdigest()
      for h in hashes:
        if h.rstrip() == new_hash:
          print p.rstrip() + ":" + hashlib.sha256(wd).hexdigest()

if __name__ == "__main__":
    crack()
