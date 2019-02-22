import socket
s = socket.socket()
s.settimeout(2)

target = 'ad.samsclass.info'
target = '142.93.136.81'

username = "foo"
password = "bar"
length = str(len(username) + len(password) + 5)

req = """POST /authenticate HTTP/1.1
Host: 1337bank.money
Connection: keep-alive
Content-Length: """

req2 = """
Cache-Control: max-age=0
Origin: http://1337bank.money
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://1337bank.money/login
Accept-Language: en-US,en;q=0.9

username="""

req3 = username + "&p=" + password

s.connect((target, 80))
s.send(req + length + req2 + req3)
print s.recv(1024)
s.close()
