# Writeup 6 - Forensics

Name: Michael Wong
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Michael Wong

## Assignment Writeup

### Part 1 (45 Pts)

1. Warmup: what IP address has been attacked?
  142.93.136.81

2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.

  The hackers performed a SYN port scan by using nmap. They were able to find vulnerable open ports. 
  SYN scan is the default and most popular scan option for good reasons. It can be performed quickly, scanning thousands of ports per second on a fast network not hampered by restrictive firewalls. It is also relatively unobtrusive and stealthy since it never completes TCP connections.

3. What are the hackers' IP addresses, and where are they connecting from?
  159.203.113.18.
  According to iplocation.net, the hackers are located in Clifton, New Jersey (40.8584, -74.1639)

4. What port are they using to steal files on the server?
  They are using a TCP port, 20 which is used for FTP

5. Which file did they steal? What kind of file is it? Provide all metadata on the file. Specifically,
  a. What kind of file is it?
    find_me.jpeg

  b.Where was this photo taken? Provide a city, state and the name of the building in your answer.
    The Hand, Rambla General Artigas, 20100 Punta Del Este, Uruguay

  c. When was this photo taken? Provide a timestamp in your answer.
    Sun, 23 December 2018 05:16:24 pm

  d. What kind of camera took this photo?
    Apple.iPhone 8 back camera 3.99mm f/1.8

  e. How high up was this photo taken? Provide an answer in meters.
    4.5726 meters above sea level

  f. Which file did the attackers leave on the server?
    greetz.fpff

  g. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is not an option.
  Change the password to a more complex password. This will prevent against a brute force attack using rockyou.txt. The attackers were able to use the username was v0idcache, and thepassword was linkinpark.


### Part 2 (55 Pts)

Parse greetz.fpff, and report the following information:
1. When was greetz.fpff generated?
  Wed Mar 27 00:15:05 2019

2. Who authored greetz.fpff?
  fl1nch

3.List each section, giving us the data in it and its type.

------- HEADER -------
MAGIC: 0x8badf00d
VERSION: 1
TIMESTAMP: Wed Mar 27 00:15:05 2019
AUTHOR: fl1nch
SECTIONS: 5
-------  BODY  -------
ASCII Output: Hey you, keep looking :)
Coordinates Output: (52.336035, 4.880673)
fpff-extracted-png.png has been created
ASCII Output: }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC
ASCII Output: Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=

Report at least one flag hidden in greetz.fpff. Any other flag found will count as bonus points towards the competition portion of the syllabus.
CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak} (inside the recovered png)
CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R} (was printed backwards)
CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding} (found by decoding final ascii to base64)

