import cv2 as cv
import numpy as np
import argparse

# read img
def load_img(img_URI):
    # loads the image as 8-bit RGB by default, -1 to include alpha channel 
    #img = cv.imread(img_URI, -1)
    img = cv.imread(img_URI)
    return img

#print(len(load_img('../btc_logo.png')[0]))
# img heigh is 256px thus we get a list of 256 rows. Width is 256px thus each row is a list of 256 rgb values

# convert each rgb value (an int) to binary

def to_bin(data):
    if isinstance(data, str):
        #print('data type:', type(data))
        return ''.join([ format(ord(i), '08b') for i in data ])
    elif isinstance(data, bytes):
        #print('data type:', type(data))
        return ''.join([ format(i, '08b') for i in data ])
    elif isinstance(data, np.ndarray):
        #print('data type:', type(data))
        return [ format(i, '08b') for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        #print('data type:', type(data))
        return format(data, '08b')
    else:
        raise TypeError('Invalid type.')

# encode 
# change the least significant bit of each rgb value 
# start with first rgb value, end when all bits of the message are encoded


def encode(img_URI, msg, delimiter):
    img_rgb = load_img(img_URI)
    msg += delimiter
    msg_to_bin = to_bin(msg)

    data_index = 0
    msg_len = len(msg_to_bin)

    for row in (img_rgb):
        for pixel in (row):
            #print(pixel[0])
            #r,g,b = to_bin(pixel)
            r = to_bin(pixel[0])
            g = to_bin(pixel[1])
            b = to_bin(pixel[2])

            if data_index < msg_len:
                pixel[0] = int(r[:-1] + msg_to_bin[data_index],2)
                data_index += 1        
            if data_index < msg_len:              
                pixel[1] = int(g[:-1] + msg_to_bin[data_index],2)
                data_index += 1
            if data_index < msg_len:              
                pixel[2] = int(b[:-1] + msg_to_bin[data_index],2)
                data_index += 1
            if data_index >= msg_len:
                break
    return img_rgb


def decode(img_URI, delimiter):
    img_rgb = load_img(img_URI)
    #print(img_rgb)

    binary_data = ''
    for row in img_rgb:
        for pixel in row:
            r, g, b = to_bin(pixel)

            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    
    bytes = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        bytes.append(byte)
    #print(bytes)
    decoded_msg = ''
    for i,byte in enumerate(bytes):
        decoded_msg += chr(int(byte, 2))
        if decoded_msg[-len(delimiter):] == delimiter:
            break
    return decoded_msg[:-len(delimiter)]

def main(img_URI, msg):
    delimiter = '===END_OF_MESSAGE_!==='
    print('[*] Start encoding...')
    encoded_img = encode(img_URI, msg, delimiter)
    cv.imwrite('encoded_img.png', encoded_img)
    print('[*] Encoding completed.')
    print('[*] Start decoding...')
    decoded_str = decode('encoded_img.png', delimiter)
    print('[*] Decoding completed. Here is your message:\n',decoded_str)
    return decoded_str

main('../btc_logo.png', 'hello world')