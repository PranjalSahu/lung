import matplotlib
matplotlib.use('TkAgg')
import pylidc as pl
import matplotlib.pyplot as plt
from skimage.measure import find_contours

ann = pl.query(pl.Annotation).first()
vol, seg = ann.uniform_cubic_resample(side_length = 100)
print(vol.shape, seg.shape)
plt.imshow(vol[:,:,50], cmap=plt.cm.gray)
contours = find_contours(seg[:,:,50], 0.5)
for contour in contours:
	plt.plot(contour[:,1], contour[:,0], '-r')
plt.show()

