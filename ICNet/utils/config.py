import numpy as np
import os

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

class Config(object):
    # Setting dataset directory
    CITYSCAPES_DATA_DIR = "/home/antonioc/Scrivania/ML/dataset/cityscape/leftImg8bit_trainvaltest"
    ADE20K_DATA_DIR = './data/ADEChallengeData2016/'

    ADE20K_eval_list = os.path.join('./data/list/ade20k_val_list.txt')
    CITYSCAPES_eval_list = "/home/antonioc/Scrivania/ML/autodeeplabVSothers/cityscapes/cityscapes_val_list.txt"

    ADE20K_train_list = os.path.join('./data/list/ade20k_train_list.txt')
    CITYSCAPES_train_list = os.path.join('./data/list/cityscapes_train_list.txt')

    IMG_MEAN = np.array((103.939, 116.779, 123.68), dtype=np.float32)

    ADE20k_param = {'name': 'ade20k',
                'num_classes': 150, # predict: [0~149] corresponding to label [1~150], ignore class 0 (background)
                'ignore_label': 0,
                'eval_size': [480, 480],
                'eval_steps': 2000,
                'eval_list': ADE20K_eval_list,
                'train_list': ADE20K_train_list,
                'data_dir': ADE20K_DATA_DIR}

    cityscapes_param = {'name': 'cityscapes',
                    'num_classes': 19,
                    'ignore_label': 255,
                    'eval_size': [1025, 2049],
                    'eval_steps': 500,
                    'eval_list': "/home/antonioc/Scrivania/ML/autodeeplabVSothers/cityscapes/cityscapes_val_list.txt",
                    'train_list': "/home/antonioc/Scrivania/ML/autodeeplabVSothers/cityscapes/cityscapes_train_list.txt",
                    'data_dir': "/home/antonioc/Scrivania/ML/dataset/cityscape/leftImg8bit_trainvaltest"}

    model_paths = {'train': '/home/antonioc/Scrivania/ML/autodeeplabVSothers/ICNet-tensorflow-master/model/cityscapes/icnet_cityscapes_train_30k.npy',
              'trainval': '/home/antonioc/Scrivania/ML/autodeeplabVSothers/ICNet//model/cityscapes/icnet_cityscapes_trainval_90k.npy',
              'train_bn': '/home/antonioc/Scrivania/ML/autodeeplabVSothers/ICNet-tensorflow-master//model/cityscapes/icnet_cityscapes_trainval_90k.npy',
              'trainval_bn': '/home/antonioc/Scrivania/ML/autodeeplabVSothers/ICNet-tensorflow-master//model/cityscapes/icnet_cityscapes_trainval_90k_bnnomerge.npy',
              'others': '/home/antonioc/Scrivania/ML/autodeeplabVSothers/ICNet-tensorflow-master//model/ade20k/model.ckpt-27150'}

    ## If you want to train on your own dataset, try to set these parameters.
    others_param = {'name': 'VOC',
                    'num_classes': 19,
                    'ignore_label': 255,
                    'eval_size': [480, 481],
                    'eval_steps': 500,
                    'eval_list': '/home/antonioc/Scrivania/ML/dataset/VOCdevkitBackup/VOC2012/ImageSets/Segmentation/val.txt',
                    'train_list': '/home/antonioc/Scrivania/ML/dataset/VOCdevkitBackup/VOC2012/ImageSets/Segmentation/train.txt',
                    'data_dir': '/home/antonioc/Scrivania/ML/dataset/VOCdevkitBackup/VOC2012/JPEGImages'}

    ## You can modify following lines to train different training configurations.
    INFER_SIZE = [1024, 2048, 3]
    TRAINING_SIZE = [480, 481]
    TRAINING_STEPS = 3000

    N_WORKERS = 12
    BATCH_SIZE = 16
    LEARNING_RATE = 1e-4
    MOMENTUM = 0.9
    POWER = 0.9
    RANDOM_SEED = 1234
    WEIGHT_DECAY = 0.0001
    SNAPSHOT_DIR = '/home/antonioc/Scrivania/ML/autodeeplabVSothers/ICNet-tensorflow-master/snapshots'
    SAVE_NUM_IMAGES = 4
    SAVE_PRED_EVERY = 500

    # Loss Function = LAMBDA1 * sub4_loss + LAMBDA2 * sub24_loss + LAMBDA3 * sub124_loss
    LAMBDA1 = 0.16
    LAMBDA2 = 0.4
    LAMBDA3 = 1.0

    def __init__(self, dataset, is_training=False, filter_scale=1, random_scale=False, random_mirror=False):
        print('Setup configurations...')

        if dataset == 'ade20k':
            self.param = self.ADE20k_param
        elif dataset == 'cityscapes':
            self.param = self.cityscapes_param
        elif dataset == 'others':
            self.param = self.others_param

        self.dataset = dataset
        self.random_scale = random_scale
        self.random_mirror = random_mirror
        self.is_training = is_training
        self.filter_scale = filter_scale

    def display(self):
        """Display Configuration values."""
        print("\nConfigurations:")
        for a in dir(self):
            if not a.startswith("__") and not callable(getattr(self, a)) and not isinstance(getattr(self, a), dict):
                print("{:30} {}".format(a, getattr(self, a)))

            if a == ("param"):
                print(a)
                for k, v in getattr(self, a).items():
                    print("   {:27} {}".format(k, v))

        print("\n")