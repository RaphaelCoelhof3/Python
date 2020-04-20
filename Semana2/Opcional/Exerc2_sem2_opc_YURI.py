segundos_entrada = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos_entrada // 86400 #divisão (INTEIRA) pela quantidade de segundos que há em 1 dia.
segs_restantes = segundos_entrada % 86400 #resto da divisão inteira feita anteriormente.

horas = segs_restantes // 3600 #os segundo que não formam um dia, serão divididos em horas.
segs_restantes_da_hora = segs_restantes % 3600 #resto de segundos que não formam 1 hora.

minutos = segs_restantes_da_hora // 60 #os segudos que não formam 1h serão divididos em minutos.
segs_restantes_final = segs_restantes_da_hora % 60 #resto dos segundos que não formam 1 min.

if (dias <= 1) and horas <=1 and minutos <= 1 and segs_restantes_final <=1 :
    
    print(dias,"dia",horas,"hora,",minutos,"minuto e",segs_restantes_final,"segundo.")

elif (dias <= 1) and horas <=1 and minutos <= 1 :

    print(dias,"dia",horas,"hora,",minutos,"minuto e",segs_restantes_final,"segundos.")

elif (dias <= 1) and horas <=1 :
    print(dias,"dia",horas,"hora,",minutos,"minutos e",segs_restantes_final,"segundos.")

elif (dias <= 1):
    print(dias,"dia",horas,"horas,",minutos,"minutos e",segs_restantes_final,"segundos.")

else :
    print(dias,"dias,",horas,"horas,",minutos,"minutos e",segs_restantes_final,"segundos.")
