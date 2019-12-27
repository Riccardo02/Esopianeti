def calcola_luminosita_stella(dati,riga,colonna,raggio):#riga e colonna del centro della stella

	riga_partenza=riga-raggio
	colonna_partenza=colonna-raggio
	
	luminosita=0
	luminosita_tot=[]
	
	for k in range(1000):#for per ogni foglio di dati
		for i in range(raggio*2+1):#for per le righe
			for j in range(raggio*2+1):#for per le colonne
	
				luminosita+=dati[k][riga_partenza+i][colonna_partenza+j]#somma tutte le luminosità
		
		luminosita_tot.append(luminosita)#salva la luminosità totale di 1 foglio in un array
		luminosita=0#si azzera per ricominciare un nuovo foglio
	
	return luminosita_tot
	



stella_1=calcola_luminosita_stella(data,100,40,5)
print(stella_1)




