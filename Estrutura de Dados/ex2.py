# 2) Crie uma função que calcula o somatório de 1/(n*n), onde o n varie na mesma faixa de valores.

import sys

def mult(n):
    result = 0
    for i in range (1, n+1):
        result = result + 1/(i*i)
    
    return result

print (mult(int(sys.argv[1])))
