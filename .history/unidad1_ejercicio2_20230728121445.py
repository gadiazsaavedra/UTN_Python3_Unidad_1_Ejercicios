"""Incorporar el modulo sys e introduccion de 3 parametros"""
import sys

if int(sys.argv[1]) % 2 == 0:
    print(f"{(sys.argv[1])} es multiplo de 2 ")
if int(sys.argv[2]) % 2 == 0:
    print(f"{(sys.argv[2])} es multiplo de 2 ")
if int(sys.argv[3]) % 2 == 0:
    print(f"{(sys.argv[3])} es multiplo de 2 ")
