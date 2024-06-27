import math

def clases_grouped(datos):
    rango = max(datos) - min(datos)
    clases = 1 + 3.3 * math.log10(len(datos))
    clases_redondear = round(clases)
    ancho = rango / clases_redondear
    
    lim_inf = [min(datos)]
    lim_sup = []
    mrks = []
    
    for i in range(clases_redondear):
        if i == 0:
            lim_sup.append(round(lim_inf[-1] + ancho, 3))
        else:
            lim_inf.append(round(lim_sup[-1], 3))
            lim_sup.append(round(lim_inf[-1] + ancho, 3))
        mrks.append(round((lim_inf[-1] + lim_sup[-1]) / 2, 3))
    
    lim_sup[-1] = max(datos)
    
    clases_num = list(range(1, clases_redondear + 1))
    
    return clases_num, [round(x, 3) for x in lim_inf], [round(x, 3) for x in lim_sup], [round(x, 3) for x in mrks]
