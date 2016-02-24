import datetime

teste = datetime.timedelta(hours=26, minutes=70)

def delta_em_horas(deltatime):
	delta = deltatime.total_seconds()
	hours, remainder = divmod(delta, 3600)
	minutes, seconds = divmod (remainder, 60)
	result = str(int(hours)).zfill(2) + ":" + str(int(minutes)).zfill(2)+ ":" +str(int(seconds)).zfill(2)
	return result


print(delta_em_horas(teste))

