#!/bin/bash
CUDA_VISIBLE_DEVICES=1 python train.py --data_name chestmnist --start_epoch 0 --end_epoch 100 --download True --net 18
CUDA_VISIBLE_DEVICES=1 python train.py --data_name chestmnist --start_epoch 0 --end_epoch 100 --download True --net 50
CUDA_VISIBLE_DEVICES=1 python train.py --data_name retinamnist --start_epoch 0 --end_epoch 100 --download True --net 18
CUDA_VISIBLE_DEVICES=1 python train.py --data_name retinamnist --start_epoch 0 --end_epoch 100 --download True --net 50