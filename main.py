def sekundni_saatga(q):
    soat = q // 3600
    daqiqa = (q % 3600) // 60
    sekund = q % 60
    return soat, daqiqa, sekund

sekund = int(input("Sekundni kiriting: "))
soat, daqiqa, sekund = sekundni_saatga(sekund)
print(f"{soat}:{daqiqa}:{sekund}")
