import cv2

a = 'datasets/inference/00_192_240_0.png'
b = 'datasets/test/hr_48/00_192_240_0.png'

ima = cv2.imread(a)
imb = cv2.imread(b)

print((ima - imb == 0).all())