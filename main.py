# Importando as bibliotecas necessárias para o projeto

import os
import pandas as pd
import matplotlib.pyplot as plt
import locale


# Definição das funções
def exibir_lista(lista):
    df = pd.DataFrame({'Arquivos': lista})
    print(f'{df}\n\n')


lista_de_arquivos = os.listdir('Curso Básico de Python/Vendas')
# exibir_lista(lista_de_arquivos)

tabela_total = pd.DataFrame()

for arquivo in lista_de_arquivos:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f'Curso Básico de Python/Vendas/{arquivo}')
        tabela_total = tabela_total._append(tabela)

# print(tabela_total)

tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
# print(tabela_produtos)

tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
# print(tabela_faturamento)

tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by='Faturamento', ascending=False)
# print(tabela_lojas)

# Módulo para visualização gráfica

# Configuração da formatação monetária
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Criação do gráfico de barras
plt.bar(tabela_lojas.index, tabela_lojas['Faturamento'])

# Adicionar os valores exatos nas barras
for i, valor in enumerate(tabela_lojas['Faturamento']):
    texto = f'R$ {locale.format_string("%.2f", valor, grouping=True)}'
    plt.text(i, valor, texto, ha='center', va='bottom')

# Configuração dos rótulos e título do gráfico
plt.xlabel('Loja')
plt.ylabel('Faturamento')
plt.title('Faturamento por Loja')

# Rotaciona os rótulos do eixo x para facilitar a leitura
plt.xticks(rotation=45)

# Exibe o gráfico
plt.show()
