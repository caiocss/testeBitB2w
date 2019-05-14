'''
Task 2
You need to count the numbers that can be created by rearranging the digits of a positive integer N
(0 < N < 109 and it has no leading zeros).
Example: there are 6 numbers that can be created by rearranging the digits of 432 and there are 4
numbers that can be formed from the number 120 (you must disconsider numbers with leading
zeros).
The code must be written in Java/Scala/Python/C and sent by e-mail.
Your program will read the input from the command line and print to the standard output. Use
args[0] to get the input (no number with leading zeros will be used for testing).

'''

import functools 
import operator
from collections import Counter
from math import factorial

#Método para capturar a quantidade de combinações possíveis sem repetição das combinações;
def qtdcombinacoes(l):
    num = factorial(len(l)) #Acha o fator conforme o tamanho da lista de numeros
    mults = Counter(l).values() #Acha a quantidades de vezes em que um numero se repete
    den = functools.reduce(operator.mul, (factorial(v) for v in mults), 1) #Acha a quantidade das repetições   
    return num / den #Remove as repetições retornando o valor de combinações

print("*********************************")
print("Teste B2W")
print("*********************************")

strNumero = input("Digite um numero: ")

numeroDividido = []

for numero in strNumero:
  numeroDividido.append(int(numero))

print(" ")
print("Quantidade de combinações possíveis:")
print(int(qtdcombinacoes(numeroDividido)))







