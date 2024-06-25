def frec_acum(fr):
    fr_acumulada = []
    fr_ac = 0

    for frecuencia in fr:
        fr_ac += frecuencia
        fr_acumulada.append(fr_ac)

    return fr_acumulada