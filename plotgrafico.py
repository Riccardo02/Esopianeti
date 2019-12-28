def creazione_grafico(stella_1):
	luminosita=np.array(stella_1)
	tempo=np.array(tempo_tot)
	plt.xlim(0,50000)
	plt.ylim(0,50000)
	plt.plot(tempo,luminosita)
	plt.ylabel('luminosità')
	plt.xlabel('tempo(s)')
	plt.show()
