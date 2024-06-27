import matplotlib.pyplot as plt

def plot_hist(clases, marcas_clase, frecuencias):
    plt.figure(figsize=(12, 6))
    plt.bar(clases, frecuencias, 
            width=1, edgecolor="k", color=["#DEE74E", "#FC8C29", "#37C5CA", "#37CA64", "#FF99F3", "#E74E50"])

    plt.xticks(clases, marcas_clase, fontsize=15, rotation=45)
    plt.xlabel("Rango de datos", fontsize=20)
    plt.ylabel("Frecuencias", fontsize=20)
    plt.title("Histograma de frecuencias por rango de datos", fontsize=25)

    plt.grid()
    plt.show()
