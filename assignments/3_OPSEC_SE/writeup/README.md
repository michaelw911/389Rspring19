# Writeup 3 - Operational Security and Social Engineering

Name: *Michael Wong*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *Michael Wong*

## Assignment Writeup

### Part 1 (40 pts)

  First off, I am assuming that I am able to figure out which bank/banks Elizabeth Moffet has a checking/savings account associated with her. If Moffet was a real person, I would find this out by looking up where she lives (via Whitepages) and making a list of the most prominent banks in that area. Whitepages typically shows all public information about a person, their address, phone number, family members, etc.

  Having a list of banks, I would impersonate as her husband, calling each bank claiming that I had been locked out of my wife's account. They would ask for the name of my wife (Moffet), and they would tell me if the account exists or not. After that they would probably ask me for verification that I am indeed Moffett husband, but it wouldn’t matter since I just need to know if the account exists or not. Like the video in lecture, I would play the crying baby sounds in the background during the call, and inform the bank representative that I need to attend to the baby once I find out the account exists.

  Knowing which bank Moffet has a checkings/savings account in, I would spoof as the bank’s security team, and email v0idcache@protonmail.com that there has been suspicious activity associated with her account and that immediate action is needed by clicking on the provided link.


  This link will redirect her to a fake webpage that imitates whatever bank she has an account in. She will be asked to put in her mother’s maiden name, city born in, and name of first pet in order to verify that it is here. Then she will be prompted to change her pin by entering her old pin, a new pin, and confirming the new pin. Since I would own the web server that she is connecting to, I would be able to find out exactly what browser she is using.

  If Moffet does not click on the link to change her information (out of suspicion or lack of checking emails), I would call her from a spoofed number with her area code (found from Whitepages), claiming to be a teller from her local bank. In the background of the call, I would be playing audio of people talking (imitate a bank). I would tell her that she needs to click the link in order to secure her account, or it will be locked.


### Part 2 (60 pts)

  Close port 1337, this port was left open for “waste”. This is a vulnerability because anybody on the internet can interact with the web server via port 1337. Utilizing the command, “nc 142.93.136.81 1337”, I am able to login into the server without any added security. Users should only be able to access the shell via ssh. In order to fix this problem, follow the guide here https://www.binarytides.com/close-open-ports-manually-in-ubuntu/

  Use a complex password, the password was very low complexity (bruteforce could find it within an hour), and is one of the most commonly breached passwords (rockyou.txt). Check your new password complexity here https://howsecureismypassword.net/. Also, we can implement a password expiration process (a new password every month) and incorrect lockout (if a user gets the password wrong too many times).

  Blacklist users who use nmap. People who perform an entire nmap scan on you system are more often than not up to no good. Most websites automatically blacklist users who perform nmap scans on their servers. An nmap scan informs users on the status of anyport within your webserver. Steps to prevent nmap scans can be found here https://success.trendmicro.com/solution/TP000087920-How-do-I-block-NMAP-port-scans

