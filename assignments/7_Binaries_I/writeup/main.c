/*
 * Name: *Michael Wong*
 * Section: *0201*
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: *Michael Wong*
 */

/* your code goes here */


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

