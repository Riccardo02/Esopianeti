#coding: utf-8
from astropy.io import fits
import json
from datetime import datetime
import os

def prendi_json(path):
	dati=json.load(open(path,"r"))
	return dati
	
	
def salva_json(dati,path):
	with open(path,"w") as outfile:
		json.dump(dati,outfile,indent=8)
	return


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








indirizzo='level_1.fits'
hdu=fits.open(indirizzo)
data=hdu[0].data
stelle_tot={}

video=str(input("Nome Video -> "))
os.system("vlc Video/" + video + ".mpg &")
os.system("vlc Video/" + video + "diff.mpg &")

for i in range(int(input("Quante stelle? "))):
	stelle_tot["stella_"+str(i+1)]=calcola_luminosita_stella(data,int(input("X stella ")),int(input("Y stella ")),int(input("raggio ")))
	print("Fatto!\nProssima stella\n")

contatore=prendi_json("Contatore/Contatore.json")


salva_json(stelle_tot,"Dati/File"+str(contatore["contatore"])+".json")


contatore["contatore"]+=1

salva_json(contatore,"Contatore/Contatore.json")

os.system("python Grafico.py &")

