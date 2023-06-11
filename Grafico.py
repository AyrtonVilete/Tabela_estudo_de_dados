import matplotlib.pyplot as plt

anos = [2020, 2021]
taxa_abandono_ensino_fundamental = [1.0, 1.2]

# Gráfico de barras: Taxa de abandono no ensino fundamental em 2020 e 2021
plt.figure()
plt.bar(anos, taxa_abandono_ensino_fundamental)
plt.xlabel('Ano')
plt.ylabel('Taxa de Abandono (%)')
plt.title('Taxa de Abandono no Ensino Fundamental (2020-2021)')

# Exibir os gráficos
plt.show()