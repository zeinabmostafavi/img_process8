import cv2
import random
import argparse
import numpy as np

d_path = argparse.ArgumentParser()
d_path.add_argument('--image')
d_path.add_argument('--output_path')
args = d_path.parse_args()


def Encryption_img():
    img = cv2.imread(f'{args.image}', cv2.IMREAD_GRAYSCALE)
    row, col = img.shape
    key = np.zeros((row, col), dtype=int)
    encripted = np.zeros((row, col), dtype=int)

    for i in range(row):
        for j in range(col):
            key[i, j] = random.randint(0, 255)
    np.save(f'{args.output_path}/key.npy', key)
    for m in range(row):
        for n in range(col):
            if (img[m, n] + key[m, n]) > 255:
                encripted[m, n] = img[m, n] + key[m, n] - 255
            else:
                encripted[m, n] = img[m, n] + key[m, n]
    cv2.imwrite(f'{args.output_path}/encrypted.bmp', encripted)


Encryption_img()
