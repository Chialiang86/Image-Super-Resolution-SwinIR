#!/bin/bash
if [ $1 = "train" ]; then
    echo task : $1
    config='options/swinir/train_swinir_sr_classical.json'
    python3 main_train_psnr.py --opt $config

elif [ $1 = "test" ]; then
    echo task : $1
    runnning_id=$2
    model_root='superresolution/swinir_sr_classical_patch48_x3_crop_1/models'
    model_ids=("205000_G" "210000_G")
    inference="inference_${2}"
    imsize=48
    crop='no'

    for model_id in ${model_ids[@]}; do
        echo "model id :" ${model_id}
        python3 main_test_swinir.py --task classical_sr \
            --scale 3 \
            --training_patch_size "${imsize}" \
            --inf_root $inference \
            --model_path "${model_root}/${model_id}.pth" \
            --folder_lq 'dataset/testing_lr_images'
        echo "zip ${inference}/${model_id}.zip ${inference}/${model_id}_${imsize}_3/*.png"

        if [ $crop = "yes" ]; then
            python3 puzzle.py -s "${inference}/${model_id}_${imsize}_3"
        fi

    done

else 
    echo "error argument : " $1
fi