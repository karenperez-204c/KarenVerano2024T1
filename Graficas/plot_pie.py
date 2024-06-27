import matplotlib.pyplot as plt

def plot_pie(datos, marcas_texto):
    plt.figure(figsize=(8, 8))
    plt.pie(datos,
            counterclock=False, 
            startangle=90, 
            autopct="%0.1f%%", 
            pctdistance=0.8, 
            colors=["#37CA64", "#FF99F3", "#37C5CA", "#E74E50", "#FC8C29", "#DEE74E"], 
            labels=marcas_texto)
    plt.title("Distribución de Sabores", fontsize=20)
    plt.show()