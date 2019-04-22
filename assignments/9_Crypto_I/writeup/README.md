# Crypto I Writeup

Name: Michael Wong
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Michael Wong

## Assignment Writeup

### Part 1 (70 Pts)

I was able to crack the following passwords:

freedom:52e5a82e5763533be232e82482d3e6f44118f88b1b6bd3224134341979fe43cc
password:739145a8634b184276559a2f3055353db3b261109649ef78445149415f0b4dee
1234567890:f3a885dd12d13ad8e58b5f6c10730a720f61103f651dfb0f49670bad8c7305d5
westside:518499174f0754eaf5421fdc17499bc8865b4c6419fbf616f17d38eb741073aa
superman:7e4096245b7ce7689e665c9054d612c1894ad0d182b60b5a9be1c8b10e817306
whatever:833c3b30b541406a644932cd498fb4d85c65f11e4968333be659c31812d2d6be
nicole:dbec1495345f5a1573a0dd437c207cacc844f74b8a7b030c858f4f660bf9484f
shadow:3f6c2527aa5f8eb3ae4bd5b33d772ba819196a95f09ad430c67c3b5b9570711e
welcome:3d925228586369644c84ae5da6753faf8109db1f725c60ccb6dffb914797d289
matrix:247ead31de7efd5c8fd859630ecb959c4e6240646fcd4d41962f25b1fb33c702

I was able to get these passwords and their associated hashes by using my crack.py. While doing so, I had to use '.rstrip()' in order to delete the new line character in creating and comparing hashes.

### Part 2 (30 Pts)

CMSC389R-{h@sh1ng_@nd_sl@sh1ng}

Output:
can you crack this hash?

d516778c9a6621a800faf9a159c9c67b6e83bcd7ee5a35e40f38915ba053d6b3
>>>
Password is westrella
how about this hash?

fc02a8c9384d5fc034f2a392293aed96acfb868b0db3beb18bc43791e393d1bb
>>>
Password is acomputer
and this hash?

3412c89f499cdeeda146fd906f6e6169a92fe659597649c1b17df2fc2e6543e7
>>>
Password is cmustang


