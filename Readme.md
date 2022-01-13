
# VRDL-HW4 Image Super Resolution
- contest link : [codalab](https://codalab.lisn.upsaclay.fr/competitions/622?secret_key=4e06d660-cd84-429c-971b-79d15f78d400)

#### Environment
- python : 3.7 (conda)
- OS : Ubuntu20.04
- CUDA Version : 11.5
- CUDA Driver Version : 495.46

#### packages
* hdf5storage==0.1.18
* matplotlib==3.4.3
* numpy==1.20.0
* opencv_python==4.5.4.58
* pandas==1.3.4
* requests==2.22.0
* scikit_image==0.18.3
* scipy==1.7.2
* timm==0.4.12
* torch==1.10.0
* torchvision==0.11.1
* tqdm==4.62.3

## Installation
#### 1. Clone GitHub Repo
```shell 
git clone https://github.com/Chialiang86/Image-Super-Resolution-SwinIR
cd SwinIR/
```

#### 2. Download dataset

- link : [google drive](https://drive.google.com/file/d/1GL_Rh1N-WjrvF_-YOKOyvq0zrV6TF4hb/view)
    - training data : 291 high-resolution images
    - testing data : 14 low-resolution images (for scoring)

## Training
- For the training process, I applied [KAIR](https://github.com/Chialiang86/Image-Super-Resolution-SwinIR/tree/master/KAIR_SwinIR), which was an open source project contained implementations of some SATO image super resolution methods like : USRNet, DnCNN, FFDNet, SRMD, DPSR, MSRResNet, ESRGAN, BSRGAN, SwinIR
- I used SwinSR as my major training architecture.
- There are two kinds of training data : 
    1. raw image data in `dataset/training_hr_images`
    2. partitioned image data in `dataset/hr_[imsize]` 
        - the partitioned images can be generated by executing `python3 training_patch.py -r dataset -s training_hr_images -hr [imgsize]`
        - ex : `python3 training_patch.py -r dataset -s training_hr_images -hr 144`
    3. modify config files (`config/train_swinir_sr_classical.json`)
        - `task`, `gpu_ids`, `scale`, `dataroot_H`, `dataroot_L`, `H_size`, `dataloader_batch_size`, `netG` (`upscale`, `img_size`)...
#### 1. Go to `SwinIR/`
``` 
cd SwinIR/
```
#### 2. Run shell script `run.sh` for training

```shell
chmod +x run.sh 
./run.sh train    # do not use "sh run.sh"
```

- You can also execute `main_train_psnr.py`
```shell 
python3 main_train_psnr.py --opt config/train_swinir_sr_classical.json
```

```
22-01-12 21:05:54.521 : <epoch:  0, iter:     200, lr:2.000e-04> G_loss: 2.309e-01
.
.
.
22-01-12 21:13:46.927 : <epoch:  0, iter:   5,000, lr:2.000e-04> G_loss: 4.201e-02 
22-01-12 21:13:46.927 : Saving the model.
22-01-12 21:13:47.595 : ---1-->  12003.png | 26.49dB
22-01-12 21:13:47.920 : ---2-->  12074.png | 29.24dB
22-01-12 21:13:48.200 : ---3-->  15004.png | 23.70dB
22-01-12 21:13:48.475 : ---4-->  15088.png | 24.71dB
22-01-12 21:13:48.778 : ---5-->  16052.png | 32.03dB
22-01-12 21:13:49.114 : ---6-->   2092.png | 28.44dB
22-01-12 21:13:49.446 : ---7-->   8049.png | 26.54dB
22-01-12 21:13:49.748 : ---8-->   8143.png | 19.60dB
22-01-12 21:13:49.789 : <epoch:  0, iter:   5,000, Average PSNR : 26.34dB
```

### 3. Models will be save in `task` specified in config json file

## Testing
#### 1. Go to `SwinIR/`
``` 
cd SwinIR/
```
#### 2. Run shell script `run.sh` for training
Modify `run.sh`
- The `model_root` folder and the model array `model_ids` in `run.sh`, ex : 
```shell 
model_root='superresolution/swinir_sr_classical_patch48_x3_crop_1/models'
model_ids=("100000_G" "105000_G" "110000_G" "115000_G" "120000_G" "125000_G" "130000_G" "135000_G" "140000_G" "145000_G" "150000_G")
```
- `imsize` is **low-resolution** image size during training (ex : hr = 144 -> lr = **48**)
- The inference result will be saved in the `inference_{running_id}/{model_id}_{imsize}_3`
- If you use cropping image data for training (ex : `dataset/hr_144`), please set `crop="yes"` 

```shell 
chmod +x run.sh 
./run.sh test 3    # do not use "sh run.sh"
```

## Reproduce the best result

#### 1. Download the best weight `100000_G.pth` from [google drive](https://drive.google.com/file/d/1prF-r7SGpvaDs6E1bjpR8hxH9jV0Ppb5/view?usp=sharing)

#### 2. Move `100000_G.pth` to `SwinIR/`

#### 3. Run shell script
```shell 
chmod +x run.sh 
./run.sh best    # do not use "sh run.sh"
```

#### 4. Result images will be save in `best/100000_G_48_3`


## Reference
```
@inproceedings{liang2021swinir,
title={SwinIR: Image Restoration Using Swin Transformer},
author={Liang, Jingyun and Cao, Jiezhang and Sun, Guolei and Zhang, Kai and Van Gool, Luc and Timofte, Radu},
booktitle={IEEE International Conference on Computer Vision Workshops},
year={2021}
}
@inproceedings{zhang2021designing,
title={Designing a Practical Degradation Model for Deep Blind Image Super-Resolution},
author={Zhang, Kai and Liang, Jingyun and Van Gool, Luc and Timofte, Radu},
booktitle={IEEE International Conference on Computer Vision},
year={2021}
}
@article{zhang2021plug, % DPIR & DRUNet & IRCNN
  title={Plug-and-Play Image Restoration with Deep Denoiser Prior},
  author={Zhang, Kai and Li, Yawei and Zuo, Wangmeng and Zhang, Lei and Van Gool, Luc and Timofte, Radu},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year={2021}
}
@inproceedings{zhang2020aim, % efficientSR_challenge
  title={AIM 2020 Challenge on Efficient Super-Resolution: Methods and Results},
  author={Kai Zhang and Martin Danelljan and Yawei Li and Radu Timofte and others},
  booktitle={European Conference on Computer Vision Workshops},
  year={2020}
}
@inproceedings{zhang2020deep, % USRNet
  title={Deep unfolding network for image super-resolution},
  author={Zhang, Kai and Van Gool, Luc and Timofte, Radu},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
  pages={3217--3226},
  year={2020}
}
@article{zhang2017beyond, % DnCNN
  title={Beyond a gaussian denoiser: Residual learning of deep cnn for image denoising},
  author={Zhang, Kai and Zuo, Wangmeng and Chen, Yunjin and Meng, Deyu and Zhang, Lei},
  journal={IEEE Transactions on Image Processing},
  volume={26},
  number={7},
  pages={3142--3155},
  year={2017}
}
@inproceedings{zhang2017learning, % IRCNN
title={Learning deep CNN denoiser prior for image restoration},
author={Zhang, Kai and Zuo, Wangmeng and Gu, Shuhang and Zhang, Lei},
booktitle={IEEE conference on computer vision and pattern recognition},
pages={3929--3938},
year={2017}
}
@article{zhang2018ffdnet, % FFDNet, FDnCNN
  title={FFDNet: Toward a fast and flexible solution for CNN-based image denoising},
  author={Zhang, Kai and Zuo, Wangmeng and Zhang, Lei},
  journal={IEEE Transactions on Image Processing},
  volume={27},
  number={9},
  pages={4608--4622},
  year={2018}
}
@inproceedings{zhang2018learning, % SRMD
  title={Learning a single convolutional super-resolution network for multiple degradations},
  author={Zhang, Kai and Zuo, Wangmeng and Zhang, Lei},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
  pages={3262--3271},
  year={2018}
}
@inproceedings{zhang2019deep, % DPSR
  title={Deep Plug-and-Play Super-Resolution for Arbitrary Blur Kernels},
  author={Zhang, Kai and Zuo, Wangmeng and Zhang, Lei},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
  pages={1671--1681},
  year={2019}
}
@InProceedings{wang2018esrgan, % ESRGAN, MSRResNet
    author = {Wang, Xintao and Yu, Ke and Wu, Shixiang and Gu, Jinjin and Liu, Yihao and Dong, Chao and Qiao, Yu and Loy, Chen Change},
    title = {ESRGAN: Enhanced super-resolution generative adversarial networks},
    booktitle = {The European Conference on Computer Vision Workshops (ECCVW)},
    month = {September},
    year = {2018}
}
@inproceedings{hui2019lightweight, % IMDN
  title={Lightweight Image Super-Resolution with Information Multi-distillation Network},
  author={Hui, Zheng and Gao, Xinbo and Yang, Yunchu and Wang, Xiumei},
  booktitle={Proceedings of the 27th ACM International Conference on Multimedia (ACM MM)},
  pages={2024--2032},
  year={2019}
}
@inproceedings{zhang2019aim, % IMDN
  title={AIM 2019 Challenge on Constrained Super-Resolution: Methods and Results},
  author={Kai Zhang and Shuhang Gu and Radu Timofte and others},
  booktitle={IEEE International Conference on Computer Vision Workshops},
  year={2019}
}
@inproceedings{yang2021gan,
    title={GAN Prior Embedded Network for Blind Face Restoration in the Wild},
    author={Tao Yang, Peiran Ren, Xuansong Xie, and Lei Zhang},
    booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
    year={2021}
}
```