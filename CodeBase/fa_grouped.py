def fa_grouped(lim_inf, lim_sup, datos):
    frecuencias = [0] * len(lim_inf)

    for dato in datos:
        for i in range(len(lim_inf)):
            if lim_inf[i] <= dato < lim_sup[i]:  # Para todos menos el último intervalo
                frecuencias[i] += 1
                break
            elif i == len(lim_inf) - 1 and lim_inf[i] <= dato <= lim_sup[i]:  # Para el último intervalo
                frecuencias[i] += 1
                break