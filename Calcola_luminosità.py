
# -*- coding: utf-8 -*-

from astropy.io import fits
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

def calcola_luminosita_stella(dati,colonna,riga,raggio):#riga e colonna del centro della stella

	dati_tot={"tempo_tot":[],"luminosita_tot":[]}
	
	riga_partenza=riga-raggio
	colonna_partenza=colonna-raggio
	
	riga_arrivo=riga+raggio
	colonna_arrivo=colonna+raggio
	
	if (riga_partenza<0 or riga_arrivo>128 or colonna_partenza<0 or colonna_arrivo>128):
		dati_tot["tempo_tot"].append(0)
		dati_tot["luminosita_tot"].append(0)
		return dati_tot#se le coordinate vanno fuori dalla matrice di dati, ritornerà un valore di 0 che non verrà visualizzato nel grafico
	
	luminosita=0
	
	tempo=0
	
	for k in range(1000):#for per ogni foglio di dati
		for i in range(raggio*2+1):#for per le righe
			for j in range(raggio*2+1):#for per le colonne
	
				luminosita+=dati[k][riga_partenza+i][colonna_partenza+j]#somma tutte le luminosità
				

		dati_tot["luminosita_tot"].append(luminosita)#salva la luminosità totale di 1 foglio in un array
		dati_tot["tempo_tot"].append(tempo)
		tempo+=50
		luminosita=0#si azzera per ricominciare un nuovo foglio
	
	
	
	return dati_tot


def creazione_grafico(stelle):
	
	n_stelle=len(stelle)
	plt.title('stelle')
	plt.xlim(0,50000)
	plt.ylim(0,50000)
	
	colori=['r','g','b','c','m','y','k']
	
	for i in range(n_stelle):
		plt.plot(stelle["stella_"+str(i+1)]["tempo_tot"],stelle["stella_"+str(i+1)]["luminosita_tot"],colori[i])
	plt.ylabel('luminosità')
	plt.xlabel('tempo(s)')
	plt.show()





indirizzo='level_1.fits'
hdu=fits.open(indirizzo)
data=hdu[0].data
stelle_tot={}



for i in range(int(input("Quante stelle? "))):
	stelle_tot["stella_"+str(i+1)]=calcola_luminosita_stella(data,int(input("X stella ")),int(input("Y stella ")),int(input("raggio ")))
	print("Fatto!\nProssima stella\n")




creazione_grafico(stelle_tot)



