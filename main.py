+# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def mensagem():
    mensagem_inicial = str(input("Insira a mensagem que em código ASCII com até 8 bits"))
    return mensagem_inicial


def chave_criptografica():
    chave = str(input("Insira o valor da chave de oito bits: \t"))
    return chave


def xor(mensagem_bits, chave):
    mensagem_encriptada = []
    for i in range(0, 8, 1):
        if mensagem_bits[i] == chave[i]:
            mensagem_encriptada.append('0')
        else:
            mensagem_encriptada.append('1')

    return mensagem_encriptada


'''MAIN'''
mensagem = mensagem()
chave = chave_criptografica()
mensagem_cifrada = xor(mensagem, chave)
print('A mensagem encripatada é:{m}' .format(m = mensagem_cifrada) )


