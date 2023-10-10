
def cripto(msg, key, mode):
    result = []
    splitedMsg = msg.split()

    if mode: # cifra
        algorithm = lambda x: chr(ord(x)+key)
    else: # decifra
        algorithm = lambda x: chr(ord(x)-key)

    for token in splitedMsg:
        # ord(str) transform character in ASCII
        # chr(int) transform ASCII in character
        tokenTransformed = map(algorithm, list(token))
        tokenTransformed = ''.join(tokenTransformed) # list -> str
        result.append(tokenTransformed)

    return ' '.join(result)

# Main
mensagem = 'Minha mensagem super secreta'
chave = 4
msgCifrada = cripto(mensagem, chave, True)
print('Mensagem cifrada: ',msgCifrada)

mensagemDecifrada = cripto(msgCifrada, chave, False)
print('Mensagem decifrada: ',mensagemDecifrada)