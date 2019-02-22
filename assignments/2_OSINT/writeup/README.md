# Writeup 2 - OSINT

Name: *Michael Wong*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *Michael Wong*

## Assignment Writeup

### Part 1 (45 pts)

*Please use this space to writeup your answers and solutions (and how you found them!) for part 1.*
  1. Realname: Elizabeth Moffet (used user sherlock to find the twitter account assocaited with v0idcache, this revealed her actual name.
  2. Where does c0idcache work: http://1337bank.money/ (located on twitter profile)
  3. List all personal information:
    - Name is Elizabeth Moffet
    - Has a twitter
    - Has a contact named "fl1nch" (from pastebin conversation)
  4. IP address:
    - 142.93.136.81 (IP)
    - 128.8.74.2 (DNS)
    - (performed nslookup 1337bank.money)
  5. Flags on website:
    - CMSC389R-{h1ding_fil3s_in_r0bots_L0L} (looking into the robots.txt and going to the secret directory)
    - CMSC389R-{h1dd3n_1n_plain_5ight} (inspect element on the home page)
  6. Open ports on website:
    - PORT    STATE    SERVICE
      22/tcp  open     ssh
      80/tcp  open     http
      1337/tcp  open     waste (gathered from nmap -p-)
  7. What operating syste is running on the website:
    - Ubuntu-4ubuntu0.2 (got this from shodan)
  8. Bonus Flags
    - "CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}" (DNS-Dumpster)


### Part 2 (75 pts)
  1. Flag:
   - CMSC389R-{brut3_f0rce_m4ster}
   - CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh} (located in AB4300.txt, file mentioned on pastebin)

  2. Approach Explanation
   - I was able to get into the web server by creating and running a bruteforce socket python script that tried passwords form the rockyou.txt (a file of the most common passwords that have been found in breaches). I targerted an port 1337, a port left open for "waste", with the username "v0idcache". I knew I found the correct password once I was got "success" and was ble to access the system shell after providing credentials through "nc 142.93.136.81 1337". Inside the system shell, I was able to locate the file /home/flag.txt, finding CMSC389R-{brut3_f0rce_m4ster}. Inside of /home/files/, I was to locate the file, AB4300.txt, a file that was deemed important form a pastebin conversation, CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}. Source code in located in a file called "stub.py"
