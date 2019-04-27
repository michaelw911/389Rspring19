#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
<<<<<<< HEAD
  hashes = open("../hashes.txt", "r").readlines()
  passwords = open("../passwords.txt", "r").readlines()
  characters = string.ascii_lowercase
  server_ip = "134.209.128.58"
  server_port = 1337

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((server_ip, server_port))
  data = s.recv(1024)

  print (data)

  while "this hash?\n" in data:
    data_arr = data.splitlines()
    server_hash = data_arr[2]

    for c in characters:
      for password in passwords:
        wd = c + password.rstrip()
        resp = hashlib.sha256(wd).hexdigest()
        if resp == server_hash:
          print "Password is " + wd
          time.sleep(2)
          
          s.send(wd+"\n")
          time.sleep(2)

          data = s.recv(1024)
          time.sleep(2)
          print(data)
          time.sleep(2)
          break
        
  s.close()
  return

=======
    hashes = # open and read hashes.txt
    passwords = # open and read passwords.txt
    characters = string.ascii_lowercase
    server_ip = 'put_your_ip_here'
    server_port = 00000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024)
    # parse data
    # crack 3 times
>>>>>>> upstream/master

if __name__ == "__main__":
    server_crack()
