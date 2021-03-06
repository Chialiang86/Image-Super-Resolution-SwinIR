#!/bin/bash
if [ $1 = "train" ]; then
    echo task : $1
    config='config/train_swinir_sr_classical.json'
    python3 main_train_psnr.py --opt $config

elif [ $1 = "test" ]; then
    echo task : $1
    runnning_id=$2
    imsize=48
    model_root="superresolution/swinir_sr_classical_patch${imsize}_x3_crop_3/models"
    model_ids=("200000_G" "250000_G" "300000_G")
    inference="inference_${2}"
    crop='no'

    for model_id in ${model_ids[@]}; do
        echo "model id :" ${model_id}
        python3 main_test_swinir.py --task classical_sr \
            --scale 3 \
            --training_patch_size "${imsize}" \
            --inf_root $inference \
            --model_path "${model_root}/${model_id}.pth" \
            --folder_lq 'dataset/testing_lr_images'

        if [ $crop = "yes" ]; then
            python3 puzzle.py -s "${inference}/${model_id}_${imsize}_3"
        fi

    done

elif [ $1 = "best" ]; then
    python3 inference.py --task classical_sr \
            --scale 3 \
            --training_patch_size 48 \
            --inf_root best \
            --model_path "100000_G.pth" \
            --folder_lq 'dataset/testing_lr_images'

elif [ $1 = "crop" ]; then
    echo "task : $1"
    echo "img size : $2"
    python3 training_patch.py -r dataset -s training_hr_images -hr $2 
else 
    echo "error argument : " $1
fi