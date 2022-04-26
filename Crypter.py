# cryptoFn = função para criptografar ou desencriptação
from asyncore import write
from turtle import right


def change_files(filename, cryptoFn, block_size=16):

    with open(file_name, 'r+b') as _file:
        raw_value = _file.read(block_size)

        while raw_value:
            cipher_value = cryptoFn(raw_value)
            # Comparar o tamanho do bloco cifrado do valor real
            if len(raw_value) != len(cipher_value):
                raise ValueError('O valor cifrado {} tem um tamanho diferente do tamanho real {}'.format
                (len(cipher_value), len(raw_value))

            _file.seek(- len(raw_value), 1)
            _file.write(cipher_value)
            raw_value = _file.read(block.size)
        