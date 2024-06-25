import math

def clases_grouped(datos):
    rango = max(datos) - min(datos)
    clases = 1 + 3.3 * math.log10(len(datos))
    clases_redondear = round(clases)
    ancho = rango / clases_redondear
    
    lim_inf = [min(datos) + i * ancho for i in range(clases_redondear)]
    lim_sup = [min(datos) + (i + 1) * ancho for i in range(clases_redondear)]
    mrks = [(lim_inf[i] + lim_sup[i]) / 2 for i in range(clases_redondear)]
    
    clases_num = list(range(1, clases_redondear + 1))
    
    return clases_num, [round(x, 3) for x in lim_inf], [round(x, 3) for x in lim_sup], [round(x, 3) for x in mrks]
