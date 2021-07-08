import cv2
import random
import argparse
import numpy as np

d_path = argparse.ArgumentParser()
d_path.add_argument('--image')
d_path.add_argument('--output_path')
args = d_path.parse_args()


def Decryption_img():
    decrypted = cv2.imread(
        f'{args.encrypted}', cv2.IMREAD_GRAYSCALE)
    row, col = decrypted.shape
    key = np.load(f'{args.key}')

    for k in range(row):
        for l in range(col):
            if (decrypted[k, l] - key[k, l]) < 255:
                decrypted[k, l] = decrypted[k, l] - key[k, l] + 255
            else:
                decrypted[k, l] = decrypted[k, l] - key[k, l]

    cv2.imwrite(f'{args.output_path}/decripted.png', decrypted)


Decryption_img()
