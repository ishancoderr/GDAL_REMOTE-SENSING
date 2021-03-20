# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 21:37:07 2021

@author: WERA
"""
import rasterio
from rasterio.plot import show
from matplotlib import pyplot as plt
import numpy as np
img_band8=rasterio.open('E:\sentinal-2\L2A_T44NMM_A028530_20201208T050600_2020-12-08_con\RT_T44NMM_A028530_20201208T050600_B08.tif')

img_band4=rasterio.open('E:\sentinal-2\L2A_T44NMM_A028530_20201208T050600_2020-12-08_con\RT_T44NMM_A028530_20201208T050600_B04.tif')


print("cordinate reference system",img_band8.crs)
metadata=img_band8.meta
print('Metadata:{metadata}\n'.format(metadata=metadata))

desccription_aboutimg=img_band8.descriptions
print('Raster description:{des}\n'.format(des=desccription_aboutimg))

print("Geotransform:",img_band8.transform)
red_img =img_band4.read(1, out_shape=(1, int(img_band4.height // 2), int(img_band4.width // 2)))


#Extract smaller region, otherwise when we do NDVI math we divide by 0 where there is no data
red_img = red_img[1000:6000, 1000:6000]

nir_img = img_band8.read(1, out_shape=(1, int(img_band8.height // 2), int(img_band8.width // 2)))
nir_img = nir_img[1000:6000, 1000:6000]

red_img_float = red_img.astype('float64') #Float 32
nir_img_float = nir_img.astype('float64')
ndvi = (nir_img_float - red_img_float) / (nir_img_float + red_img_float)
plt.imshow(ndvi)
plt.colorbar()