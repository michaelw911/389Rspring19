# Writeup 7 - Binaries I

Name: *Michael Wong*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Michael Wong*

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
#include <stdio.h>

int main () {
  int a =  0xfeedface;
  int b = 0x1ceb00da;

  char *a_fmt = "a = %d\n"; /* converts form hex to dec */
  char *b_fmt = "b = %d\n";

  printf(a_fmt, a);
  printf(b_fmt, b);

  a = a^b; /* switches a and b */
  b = b^a;
  a = a^b;

  printf(a_fmt, a);
  printf(b_fmt, b);

  return 0;
}


Output:
a = -17958194
b = 485163226
a = 485163226
b = -17958194
```

### Part 2 (10 Pts)

My program stores the hex values of 0xfeedface and 0x1ceb00da as int variables: a [rbp-0x4] and b respectfully [rbp-0x8]. It then prints the orgina; values of a and b in decimal form. Then swaps the values of a and b, and prints them again in decimal form.

