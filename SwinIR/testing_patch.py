import cv2
import os
from tqdm import tqdm
import argparse


def main(args):

    src_path = f'{args.root}/{args.src}/'
    dst_path = f'{args.root}/{args.tar}/'

    if not os.path.exists(src_path):
        raise Exception(f'src dir : {src_path} not exists')
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
        print(f'{dst_path} created.')

    img_files = os.listdir(src_path)
    for img_file in tqdm(img_files):
        hr_img = cv2.imread(f'{src_path}/{img_file}')
        size = hr_img.shape[:2]

        # high resolution
        hh_num = size[0] // args.size + 1
        hw_num = size[1] // args.size + 1
        lid = 0
        for hi in range(hh_num):
            for wi in range(hw_num):
                # case 1
                if hi == hh_num - 1 and wi == hw_num - 1:
                    hr_crop = hr_img[-args.size:, -args.size:]
                # case 2
                elif hi == hh_num - 1:
                    hr_crop = hr_img[-args.size:,
                                     (wi * args.size): (wi * args.size + args.size)]
                # case 3
                elif wi == hw_num - 1:
                    hr_crop = hr_img[(hi * args.size): (hi * \
                                      args.size + args.size), -args.size:]
                # case 4
                else:
                    hr_crop = hr_img[(hi *
                                      args.size): (hi *
                                                   args.size +
                                                   args.size), (wi *
                                                                args.size): (wi *
                                                                             args.size +
                                                                             args.size)]
                cv2.imwrite(
                    f'{dst_path}/{img_file[:-4]}_{size[0]}_{size[1]}_{lid}.png',
                    hr_crop)
                lid += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', '-r', default='datasets', type=str)
    parser.add_argument('--src', '-s', default='testing_lr_images', type=str)
    parser.add_argument('--tar', '-t', default='test/lr_48', type=str)
    parser.add_argument('--size', '-size', default=48, type=int)
    args = parser.parse_args()

    main(args)
