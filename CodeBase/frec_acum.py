def frec_acum(fa):
    
    fr_acumulada = []
    fr_ac = 0

    for frecuencia in fa:
        fr_ac += frecuencia
        fr_acumulada.append(fr_ac)

    return fr_acumulada
