
# -*- coding: utf-8 -*-

from astropy.io import fits
import matplotlib.pyplot as plt
indirizzo='level_1.fits'
hdu=fits.open(indirizzo)
data=hdu[0].data
ima=data[6,:,:]
plt.imshow(-ima,cmap='ocean')

for i in range(1000):
	print (i)
	ima=data[i,:,:]
	plt.imshow(-ima,cmap='ocean')
	plt.plot([1,2,3])
	plt.savefig(str(i)+'.png')


print (len(data))


plt.show()
