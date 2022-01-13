import cv2
import os
from tqdm import tqdm
import argparse


def main(args):

    src_path = f'{args.root}/{args.src}/'
    dst_hr_path = f'{args.root}/hr_{args.hr}/'

    if not os.path.exists(src_path):
        raise Exception(f'src dir : {src_path} not exists')
    if not os.path.exists(dst_hr_path):
        os.mkdir(dst_hr_path)
        print(f'{dst_hr_path} created.')

    img_files = os.listdir(src_path)
    for img_file in tqdm(img_files):
        hr_img = cv2.imread(f'{src_path}/{img_file}')
        size = hr_img.shape[:2]

        # high resolution
        hh_num = size[0] // args.hr + 1
        hw_num = size[1] // args.hr + 1
        lid = 0
        for hi in range(hh_num):
            for wi in range(hw_num):
                # case 1
                if hi == hh_num - 1 and wi == hw_num - 1:
                    hr_crop = hr_img[-args.hr:, -args.hr:]
                # case 2
                elif hi == hh_num - 1:
                    hr_crop = hr_img[-args.hr:,
                                     (wi * args.hr): (wi * args.hr + args.hr)]
                # case 3
                elif wi == hw_num - 1:
                    hr_crop = hr_img[(hi * args.hr)
                                      : (hi * args.hr + args.hr), -args.hr:]
                # case 4
                else:
                    hr_crop = hr_img[(hi *
                                      args.hr): (hi *
                                                 args.hr +
                                                 args.hr), (wi *
                                                            args.hr): (wi *
                                     args.hr +
                                     args.hr)]

                if hr_crop.shape[:2] != (args.hr, args.hr):
                    hr_crop = cv2.resize(
                        hr_crop, (args.hr, args.hr), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(
                    f'{dst_hr_path}/{img_file[:-4]}_{size[0]}_{size[1]}_{lid}.png',
                    hr_crop)
                lid += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', '-r', default='dataset', type=str)
    parser.add_argument('--src', '-s', default='training_hr_images', type=str)
    parser.add_argument('--hr', '-hr', default=96, type=int)
    args = parser.parse_args()

    main(args)
