import cv2
import os
from tqdm import tqdm

# fnames = glob.glob('datasets/sr_16_128/*.png')
src = 'datasets/training_hr_images'
dst = 'datasets/training_lr_images'
size = 144

fnames = os.listdir(src)

for fname in  tqdm(fnames):
    img = cv2.imread(f'{src}/{fname}')
    shape = img.shape[:2] 
    img_r = cv2.resize(img, (shape[1] // 3, shape[0] // 3))
    target = f'{dst}/{fname}'
    cv2.imwrite(target, img_r)