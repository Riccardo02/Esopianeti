#coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import json

def prendi_json(path):
	dati=json.load(open(path,"r"))
	return dati

def salva_json(dati,path):
	with open(path,"w") as outfile:
		json.dump(dati,outfile,indent=8)
	return

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
	

contatore=prendi_json("Contatore/Contatore.json")
if(contatore["da_solo"]=="True"):

	stelle_tot=prendi_json("Dati/File"+str(contatore["contatore"])+".json")
	contatore["da_solo"]="False"
else:
	stelle_tot=prendi_json("Dati/"+str(input("Quale file vuoi aprire?"))+".json")

salva_json(contatore,"Contatore/Contatore.json")
creazione_grafico(stelle_tot)


