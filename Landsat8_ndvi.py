# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:13:39 2021

@author: WERA
"""
import rasterio
from rasterio.plot import show
from matplotlib import pyplot as plt
import numpy as np

img_band4=rasterio.open('E:\sentinal-2\L2A_T44NMM_A028530_20201208T050600_2020-12-08_con\LC08_L1TP_042035_20180603_20180615_01_T1_B4_clip.tif')
img_band5=rasterio.open('E:\sentinal-2\L2A_T44NMM_A028530_20201208T050600_2020-12-08_con\LC08_L1TP_042035_20180603_20180615_01_T1_B5_clip.tif')

print(img_band4.height)

red_img=img_band4.read(1,out_shape=(int(img_band4.height//2),int(img_band4.width//2)))
nir_img=img_band5.read(1,out_shape=(int(img_band5.height//2),int(img_band5.width//2)))

red=red_img.astype('float64')
nir=nir_img.astype('float64')

ndvi=np.where((nir+red)==0.,0,(nir-red)/(nir+red))
plt.imshow(ndvi)
plt.colorbar()