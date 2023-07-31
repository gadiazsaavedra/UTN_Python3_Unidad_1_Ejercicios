"""Incorporar el modulo sys e introduccion de 3 parametros
luego indicar cuales son multiplos de 2"""
import sys

for arg in sys.argv[1:]:
    if int(arg) % 2 == 0:
        print(f"{arg} es multiplo de 2")
