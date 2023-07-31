"""Incorporar el modulo sys e introduccion de 3 parametros"""
import sys

print(sys.argv[0])
PARAMETRO1 = int(sys.argv[1])
PARAMETRO2 = int(sys.argv[2])
PARAMETRO3 = int(sys.argv[3])
print(type(PARAMETRO1))
print(type(PARAMETRO2))
print(type(PARAMETRO3))
if int(sys.argv[1]) % 2 == 0: print(f"{PARAMETRO1} es multiplo de 2 ")

"""Indicar si los parametros son multiplos de dos"""
# MULTIPLO = 2


def es_multiplo(numero: int, multiplo: int) -> int:
    """funcion que define si es o no multiplo"""
    return numero % multiplo == 0


if es_multiplo(PARAMETRO1, 2):
    print(f"{PARAMETRO1} Sí es múltiplo")
else:
    print(f"{PARAMETRO1} No es múltiplo")


print(sys.argv)
print(type(sys.argv))
print(len(sys.argv))
print(type(sys.argv))
print(sys.argv[1:])
mylist = sys.argv[1:]
print(mylist)
newlist = [x for x in mylist if x % 2 == 0]
print(newlist)
