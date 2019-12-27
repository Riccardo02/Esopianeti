from astropy.io import fits
import matplotlib.pyplot as plt
hdu=fits.open("level_1.fits")
data=hdu[0].data
ima=data[0,:,:]
plt.imshow(-ima,cmap='ocean')





from mpl_toolkits import mplot3d
import numpy as np
gridsize=128
fig = plt.figure()
ax = plt.axes(projection='3d')
x, y = np.meshgrid(range(gridsize), range(gridsize))
ax.plot_surface(x,y,ima,cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')
plt.show()




def calcola_luminosita_stella(dati,riga,colonna,raggio):

	riga_partenza=riga-raggio
	colonna_partenza=colonna-raggio
	
	luminosita=0
	luminosita_tot=[]
	
	for k in range(1000):
		for i in range(raggio*2+1):
			for j in range(raggio*2+1):
	
				luminosita+=dati[k][riga_partenza+i][colonna_partenza+j]
		
		luminosita_tot.append(luminosita)
		luminosita=0
	
	return luminosita_tot
	



stella_1=calcola_luminosita_stella(data,100,40,5)
print(stella_1)

