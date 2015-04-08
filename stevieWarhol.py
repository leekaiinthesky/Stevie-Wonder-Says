from skimage import data, io, segmentation, color, transform, exposure
from skimage.future import graph
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

img = io.imread('images/IMG_4080.JPG')
img = transform.resize(img, [round(img.shape[0] / 10), round(img.shape[1] / 10)])
img = img[:round(img.shape[0] * 5 / 6)]

labels1 = segmentation.slic(img, compactness=25, n_segments=200)
out1 = color.label2rgb(labels1, img, kind='avg')

equalized_red = exposure.equalize_hist(out1[:, :, 0])
equalized_green = exposure.equalize_hist(out1[:, :, 1])
equalized_blue = exposure.equalize_hist(out1[:, :, 2])

#plt.figure(figsize=(2, 2))
gs1 = gridspec.GridSpec(2, 2, 0, 0, 1, 1, 0, 0)
#gs1.update(wspace=0, hspace=0)

out0 = out1.copy()
out0[:, :, 0] = equalized_red
out0[:, :, 1] = equalized_green
ax1 = plt.subplot(gs1[0])
ax1.set_xticklabels([])
ax1.set_yticklabels([])
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
io.imshow(out1)

blue = out1.copy()
blue[:, :, (0, 1)] = 0
blue[:, :, 2] = equalized_blue
ax2 = plt.subplot(gs1[1])
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)
ax2.set_xticklabels([])
ax2.set_yticklabels([])
io.imshow(blue)

ax3 = plt.subplot(gs1[2])
ax3.get_xaxis().set_visible(False)
ax3.get_yaxis().set_visible(False)
ax3.set_xticklabels([])
ax3.set_yticklabels([])

io.imshow(equalized_blue)

out2 = out1.copy()
out2[:, :, 2] = equalized_blue
ax4 = plt.subplot(gs1[3])
ax4.get_xaxis().set_visible(False)
ax4.get_yaxis().set_visible(False)
ax4.set_xticklabels([])
ax4.set_yticklabels([])
io.imshow(out2)

io.show()

#plt.savefig('test.png', bbox_inches='tight')