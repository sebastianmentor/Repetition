import random

current_temp = 10

lista_med_temperaturer_från_en_sensor = []

antal_temperaturmätningar = 0

# while antal_temperaturmätningar < 20:
#     current_temp += random.uniform(0, 2)

#     lista_med_temperaturer_från_en_sensor.append(current_temp)
#     antal_temperaturmätningar += 1

# for temperatur in lista_med_temperaturer_från_en_sensor:
#     print(temperatur)

# for antal_ggr in range(20):
#     current_temp += random.uniform(0, 2)

#     lista_med_temperaturer_från_en_sensor.append(current_temp)
#     antal_temperaturmätningar += 1

# for temperatur in lista_med_temperaturer_från_en_sensor:
#     print(temperatur)


# listor i listor --->>> [[[]],[]]
listor_i_lista = []

for i in range(5):
    listor_i_lista.append([])
    for j in range(5):
        listor_i_lista[i].append(j + random.random())
    
print(listor_i_lista)
