import cv2
import os
import numpy as np
import argparse


def main(args):

    tar = f'{args.src}/submit'
    if not os.path.exists(tar):
        os.mkdir(tar)

    fnames = sorted(os.listdir(args.src))

    scale = int(args.src.split('_')[-1])
    patch_size = int(args.src.split('_')[-2]) * scale

    tmp_prefix = None
    target_img = None
    height = 0
    width = 0
    for fname in fnames:
        if '.png' not in fname:
            continue

        if tmp_prefix != fname.split('_')[0]:
            if target_img is not None:
                cv2.imwrite(f"{tar}/{tmp_prefix}_pred.png", target_img)
                print(f"{tar}/{tmp_prefix}.png saved.")

            tmp_prefix = fname.split('_')[0]
            height = int(fname.split('_')[1]) * scale
            width = int(fname.split('_')[2]) * scale
            target_img = np.zeros((height, width, 3))

        patch = cv2.imread(f"{args.src}/{fname}")
        assert patch.shape[:2] == (patch_size, patch_size), 'image size error'

        id = int(fname.split('_')[3].split('.')[0])
        hnum = height // patch_size + 1
        wnum = width // patch_size + 1

        if id // wnum == hnum - 1 and id % wnum == wnum - 1:
            target_img[-patch_size:, -patch_size:] = patch
        elif id // wnum == hnum - 1:
            target_img[-patch_size:, (id %
                                      wnum) * patch_size: (id %
                                                           wnum + 1) * patch_size] = patch
        elif id % wnum == wnum - 1:
            target_img[(id // wnum) * patch_size: (id // wnum + 1)
                       * patch_size, -patch_size:] = patch
        else:
            target_img[(id // wnum) * patch_size: (id // wnum + 1) * patch_size,
                       (id % wnum) * patch_size: (id % wnum + 1) * patch_size] = patch


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', '-s', default='inference', type=str)
    args = parser.parse_args()

    main(args)
