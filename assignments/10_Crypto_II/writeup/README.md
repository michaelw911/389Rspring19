# Crypto II Writeup

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (70 Pts)

CMSC389R-{m3ss@g3_!n_A_b0ttl3}

I ran the following commands:
1. 'gpg --import key.asc'  to import the key
2. 'gpg --output output --decrypt message.txt.gpg' in to find the instructions.
3.  Made my signature file
4. 'gpg --sign --clearsign signature.txt' to create signature.txt.asc

Screenshot is included: gpg_screenshot.png



### Part 2 (30 Pts)

1. Both picures are attempts to encode the hidden message by changing colors and pixel arrangement in order to distort the image to those without the right key.
The CBC picutre did not do a good job at distorting the picutre, as I can see the basic shapes that are in the original image. The ECB picture is completly unrecognizable.

2. ECB is much less secure as it can allow plaintext patterns to be seen and only encrypts the color of each indivual pixel.

CBC is much more secure as it XORs each block of plaintext with the previous cipher text block before being encrupted. The initialiation vector makes each message unique, making the encrypted message impossbile to decode by the human eye.
