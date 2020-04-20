segundos_srt = input("Por favor, entre com o número de segundos que deseja converter: ")

total_segs = int(segundos_srt)

dias = total_segs // 86400
segs_restantes = total_segs % 86400

horas = segs_restantes // 3600
segs_restantes_da_hora = segs_restantes % 3600

minutos = segs_restantes_da_hora // 60
segs_restantes_final = segs_restantes_da_hora % 60


if dias < 1:
    print(dias,"dia,",horas,"horas,",minutos,"minutos e",segs_restantes_final,"segundos.")
else:
    print(dias,"dias,",horas,"horas,",minutos,"minutos e",segs_restantes_final,"segundos.")

