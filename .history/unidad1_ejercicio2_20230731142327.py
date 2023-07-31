"""Incorporar el modulo sys e introduccion de parametros
luego indicar cuales son multiplos de 2"""
import sys

even_numbers = filter(lambda x: int(x) % 2 == 0, sys.argv[1:])

for arg in even_numbers:
    print(f"{arg} es multiplo de 2")

