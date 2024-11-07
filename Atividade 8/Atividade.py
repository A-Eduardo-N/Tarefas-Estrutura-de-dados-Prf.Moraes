horas_sono = np.array([
    [8, 6, 7, 8, 6],  # Semana 1
    [5, 5, 6, 7, 8],  # Semana 2
    [6, 7, 8, 6, 5],  # Semana 3
    [7, 5, 9, 7, 4]   # Semana 4
])
#Questão 1
dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex']
max_dia = dados.max(axis=0)
dia_max = dias[np.argmax(max_dia)]
print(f"1. O dia da semana com maior horário de descanso é: {dia_max} ({max_dia.max()} horas)")
#Questão 2
min_dia = dados.min(axis=0)
dia_min = dias[np.argmin(min_dia)]
print(f"2. O dia da semana com menor horário de descanso é: {dia_min} ({min_dia.min()} horas)")

#Questão 3
soma_semanal = dados.sum(axis=1)
semana_max = np.argmax(soma_semanal) + 1  # Adiciona 1 porque as semanas começam de 1
print(f"3. A semana com maior horário de descanso é a Semana {semana_max} ({soma_semanal.max()} horas)")

#Questão 4
semana_min = np.argmin(soma_semanal) + 1
print(f"4. A semana com menor horário de descanso é a Semana {semana_min} ({soma_semanal.min()} horas)")

#Questão 5
menor_tempo = dados.min()
print(f"5. O menor tempo de descanso é: {menor_tempo} horas")

#Questão 6
maior_tempo = dados.max()
print(f"6. O maior tempo de descanso é: {maior_tempo} horas")

#Questão 7
dias_com_menor_tempo = np.sum(dados == menor_tempo)
print(f"7. Quantos dias da semana tive com o menor tempo de descanso? {dias_com_menor_tempo} dias")

#Questão 8
dias_com_maior_tempo = np.sum(dados == maior_tempo)
print(f"8. Quantos dias da semana tive com o maior tempo de descanso? {dias_com_maior_tempo} dias")

#Questão 9
total_mes = soma_semanal.sum()
percentual_semanal = (soma_semanal / total_mes) * 100
for i, percent in enumerate(percentual_semanal, start=1):
    print(f"9. Percentagem de horas na Semana {i}: {percent:.2f}%")