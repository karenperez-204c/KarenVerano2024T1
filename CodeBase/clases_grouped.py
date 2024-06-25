import math

def clases_grouped(datos):
    min_dato = min(datos)
    max_dato = max(datos)
    rango = max_dato - min_dato
    
    clases = 1 + 3.3 * math.log10(len(datos))
    clases_redondear = round(clases)
    
    ancho = rango / clases_redondear
    
    lim_inf = [min_dato + i * ancho for i in range(clases_redondear)]
    lim_sup = [lim_inf[i] + ancho for i in range(clases_redondear)]
    mrks = [(lim_inf[i] + lim_sup[i]) / 2 for i in range(clases_redondear)]
    
  
    lim_inf = [round(x, 3) for x in lim_inf]
    lim_sup = [round(x, 3) for x in lim_sup]
    mrks = [round(x, 3) for x in mrks]
    
    clases_num = list(range(1, clases_redondear + 1))
    
    return clases_num, lim_inf, lim_sup, mrks
