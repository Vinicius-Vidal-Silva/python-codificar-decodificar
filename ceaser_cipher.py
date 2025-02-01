def encrypt(texto, shift):
    texto_original = texto
    texto_criptografado = ""
    for letra in texto_original:
        if letra in alfabeto:
            indice = alfabeto.index(letra) + shift
            if indice > 25:
                indice_reset = indice - 26
                indice = indice_reset
            elif indice < -25:
                indice_reset = 26 + indice
                indice = indice_reset
            texto_criptografado = texto_criptografado + alfabeto[indice]
        else:
            texto_criptografado = texto_criptografado + letra
    indice = 0
    return texto_criptografado

def decrypt(texto_criptografado, shift):
    texto_criptografado = texto_criptografado
    texto_traduzido = ""
    for letra in texto_criptografado:
        if letra in alfabeto:
            indice = alfabeto.index(letra) - shift
            if indice < 25:
                indice_reset = indice - 26
                indice = indice_reset
            elif indice > -25:
                indice_reset = 26 + indice
                indice = indice_reset
            texto_traduzido = texto_traduzido + alfabeto[indice]
        else:
            texto_traduzido = texto_traduzido + letra
    indice = 0
    return texto_traduzido

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Escreva 'codificar' para codificar, 'decodificar' para decodificar e 'sair' para sair:\n").lower().strip()
    if direction == 'sair':
        break
    texto = input("Escreva sua menssagem:\n").lower()
    shift = int(input("Escreva seu número de criptografia:\n"))

    if direction == 'codificar':
        resultado = encrypt(texto = texto, shift = shift)
        print(resultado)
        escolha_1 = input("Deseja decodificar o texto? Digite 'sim' ou 'nao'\n").lower().strip()
        if escolha_1 == 'sim':
            shift = int(input("Escreva seu número de criptografia:\n"))
            teste = decrypt(texto_criptografado = resultado, shift = shift)
            print(teste)
        else:
            break
    elif direction == 'decodificar':
        texto_origial = decrypt(texto_criptografado = texto, shift = shift)
        print(texto_origial)
    else:
        print('Digite uma opção válida!')

