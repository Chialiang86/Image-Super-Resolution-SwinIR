
if [ $1 = "train" ]; then
    echo task : $1
    config='options/swinir/train_swinir_sr_classical.json'

    python3 main_train_psnr.py --opt $config

elif [ $1 = "test" ]; then
    echo task : $1
    model_root='superresolution/swinir_sr_classical_patch48_x3/models'
    model_id='310000_G'
    inference='inference'
    imsize=48

    python3 main_test_swinir.py --task classical_sr \
        --scale 3 \
        --training_patch_size $imsize \
        --model_path $model_root/$model_id.pth \
        --folder_lq 'dataset/testing_lr_images' 
    cp {$model_root}/{$model_id}.pth {$inference}/{$model_id}_{$imsize}_{$svale}/{$model_id}.pth

else 
    echo "error argument : " $1
fi