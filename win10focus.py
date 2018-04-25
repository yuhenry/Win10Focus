# 保存近几天的Win10聚焦壁纸 手机壁纸和桌面壁纸分开保存

import glob
import os
import numpy as np
import cv2
import shutil

OUT_MOBILE_IMAGE_DIR = input('请输入手机壁纸保存路径： ').strip()
OUT_DESKTOP_IMAGE_DIR = input('请输入桌面壁纸保存路径： ').strip()
USR_NAME = input('请输入您计算机用户名： ')
IN_IMAGE_DIR = os.path.join('C:/Users', USR_NAME, 'AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets')

for i in glob.glob(os.path.join(IN_IMAGE_DIR, '*')):
    file_size = os.path.getsize(i)/1024
    if file_size > 420:
        file_name = os.path.join(OUT_MOBILE_IMAGE_DIR, os.path.basename(i)+'.jpg')
        shutil.copyfile(i, file_name)
        img = cv2.imread(file_name)
        print(file_name, img.shape)
        if img.shape[0] < img.shape[1]:
            shutil.move(file_name, os.path.join(OUT_DESKTOP_IMAGE_DIR, os.path.basename(file_name)))
