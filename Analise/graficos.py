import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')

info_pedidos = pd.read_csv(r".\Dados\FACT_Orders.csv")
produtos_vendidos = pd.read_csv(r".\Dados\DIM_Products.csv")
info_clientes = pd.read_csv(r".\Dados\DIM_Customer.csv")
info_entrega = pd.read_csv(r".\Dados\DIM_Delivery.csv")
carrinho = pd.read_csv(r".\Dados\DIM_Shopping.csv")

#Grafico 1 - Vendas por mês

vendas_confirmadas = info_pedidos[info_pedidos['Purchase_Status'] == 'Confirmado'].copy()
vendas_confirmadas['Order_Date'] = pd.to_datetime(vendas_confirmadas['Order_Date'])

# Traduzir meses para português
traducao = {
    'January': 'Janeiro', 'February': 'Fevereiro', 'March': 'Março',
    'April': 'Abril', 'May': 'Maio', 'June': 'Junho',
    'July': 'Julho', 'August': 'Agosto', 'September': 'Setembro',
    'October': 'Outubro', 'November': 'Novembro', 'December': 'Dezembro'
}

vendas_confirmadas['Mes'] = vendas_confirmadas['Order_Date'].dt.month_name().map(traducao)

# Contar vendas por mês
vendas_meses = vendas_confirmadas['Mes'].value_counts()

# Ordenar cronologicamente (Fev, Mar, Abr, Mai)
ordem_correta = ['Fevereiro', 'Março', 'Abril', 'Maio']
venda_mes = vendas_meses.reindex(ordem_correta)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.bar(venda_mes.index, venda_mes.values, color='skyblue', edgecolor='navy')
plt.title('Quantidade de Vendas por Mês', fontsize=16, fontweight='bold')
plt.xlabel('Meses', fontsize=12)
plt.ylabel('Número de Pedidos', fontsize=12)
plt.xticks(rotation=20)
plt.grid(axis='y', alpha=0.3)

# Adicionar os valores em cima das barras
for i, v in enumerate(venda_mes.values):
    plt.text(i, v + 2, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

#Grafico 2 - Produtos que mais vendem

produtos_mais_vendidos = carrinho['Product'].value_counts().head()

plt.figure(figsize=(10, 6))
plt.bar(produtos_mais_vendidos.index, produtos_mais_vendidos.values, color='skyblue', edgecolor='navy')
plt.title("Os itens mais vendidos", fontsize=16)
plt.xlabel("Produtos", fontsize=12)
plt.ylabel("Quantidade", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

for i, v in enumerate(produtos_mais_vendidos.values):
    plt.text(i, v + 2, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

#Grafico 3 - As formas de compras mais feitas

formas_pagamento = info_pedidos['payment'].value_counts()

# Criar gráfico de pizza

#Gráfico 3 - As formas de compras mais feitas
formas_pagamento = info_pedidos['payment'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(formas_pagamento.values, 
        labels=formas_pagamento.index, 
        autopct='%1.1f%%',
        startangle=90,
        colors=['#2ecc71', '#e74c3c', '#f39c12', '#3498db', '#9b59b6'],  # Adicione mais cores
        shadow=True,
        textprops={'fontsize': 12})

plt.title('Formas de Pagamento Mais Utilizadas', fontsize=16, fontweight='bold')  # Corrigi o título
plt.tight_layout()
plt.show()