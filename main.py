import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from skimage.measure import compare_ssim
#from core.utils import preprocess
from PIL import Image

#file_path = 'D:\yuantu'
'''def colormap():
    return mpl.colors.LinearSegmentedColormap.from_list('cmap', ['#FFFFFF', '#98F5FF', '#00FF00', '#FFFF00','#FF0000', '#8B0000'], 256)'''

#for i in range(10):
fig = plt.figure()
#file_name = file_path +'gt'+str(40+i*2)+'.png'
data = np.array(Image.open(r'D:\yuantu\convert_model6.png'))               #file_name
im = plt.imshow(data, cmap=mpl.cm.rainbow, vmin = 0, vmax = 80 )          #colormap()
plt.axis('off')
fig.colorbar(im)
fig.savefig('D:\gt\ '+str(6)+'.png')
'''
    fig = plt.figure()
    file_name = file_path + 'pd' + str(40 + i * 2) + '.png'
    data = np.array(Image.open(file_name))
    im = plt.imshow(data, cmap=mpl.cm.rainbow)
    fig.colorbar(im)
    fig.savefig('D:\pd' + str(40 + i * 2) + '.png')
'''
