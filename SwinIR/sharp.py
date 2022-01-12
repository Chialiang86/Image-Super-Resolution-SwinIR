from typing_extensions import ParamSpec
import cv2
import glob
import os
import argparse

def main(args):
    folder = os.path.join(args.root, args.src)
    f_imgs = os.list(folder)

    for f_img in f_imgs:
        img = cv2.imread(f_img)
        

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', '-r', default='inference', type=str)
    parser.add_argument('--src', '-s', default='50000_G_48_3', type=str)
    args = parser.parse_args()

    main(args)