#!/usr/bin/python3
'''
Use the ASCII alphabet, print chars in lower case, not followed by a new line.
'''

for alpha in range(97, 123):
	print("{}".format(chr(alpha)), end="")
