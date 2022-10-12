# Задача №4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc
#RLE algorithm


# RLE algorithm

def rle_compress(text_message):
    """RLE compression algorithm"""
    compress = ''
    count = 1
    i = 1
    while i <= len(text_message):

        if i == len(text_message):
            compress = compress + str(count) + str(text_message[i - 1])
        elif text_message[i-1] == " ":
            compress += " "
            count = 1
        else:
            if text_message[i] == text_message[i-1]:
                count += 1
            else:
                compress = compress + str(count) + str(text_message[i-1])
                count = 1
        i += 1
    print(f'{compress}')
    return compress


def decompress_rle(compressed):
    decompress = ''
    i = 0
    num = 1
    while i < len(compressed):
        while compressed[i].isdigit():
            num = int(compressed[i]) * num
            i += 1
        if compressed[i].isalpha():
            decompress = decompress + (compressed[i] * num)
            num = 1
        else:
            compressed[i] == " "
            decompress += " "
        i += 1
    print(decompress)
    write_file('decompressed_RLE.txt', decompress)


def write_file(file_name, text_message):

    file = open(file_name, "w")
    compressed_text = rle_compress(text_message)
    file.write(compressed_text)
    file.close()


def open_file(file_name):
    file = open(file_name, "r")
    compress_text = file.read()
    decompress_rle(compress_text)
    file.close()


if __name__ == '__main__':

 
    print("*"*80)
    write_file('compressed_RLE.txt', 'BBBBBBBBB AAkkkVVV TTTTTUUU')
    open_file('compressed_RLE.txt')
