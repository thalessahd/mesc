# 1) Crie uma função que calcula o somatório de 1/n, onde o n varie de 1 até 100.
import sys

def sum(n):
    result = 0
    for i in range (1, n+1):
        result = result + 1/i
    
    return result

print (sum(int(sys.argv[1])))
