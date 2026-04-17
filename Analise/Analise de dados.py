import pandas as pd
import numpy as np

info_pedidos = pd.read_csv(r".\Dados\FACT_Orders.csv")
produtos_vendidos = pd.read_csv(r".\Dados\DIM_Products.csv")
info_clientes = pd.read_csv(r".\Dados\DIM_Customer.csv")
info_entrega = pd.read_csv(r".\Dados\DIM_Delivery.csv")
carrinho = pd.read_csv(r".\Dados\DIM_Shopping.csv")

#Analisar primeiro as informações dos pedidos para ver se tem outliers
print(info_pedidos.describe().loc[['mean', '25%', '50%', '75%', 'max']])

#25%
Q1 = info_pedidos['Total'].quantile(0.25)
#75%
Q3 = info_pedidos['Total'].quantile(0.75)
IQR = Q3 - Q1

#Definindo o limte superior para analisar outliers
limite_superior = Q3 + (1.5 * IQR)

#Analisando os pedidos que são mais feitos
pedidos_normais = info_pedidos[info_pedidos['Total'] <= limite_superior]

#Analisando os pedidos menos comuns e altos
pedidos_vip = info_pedidos[info_pedidos['Total'] > limite_superior]

#Variavel para analisar o faturamento nas compras
Faturamento = info_pedidos.loc[info_pedidos['Purchase_Status'] == 'Confirmado', 'Total'].sum()

#Variavel para analisar o dia e o mês que mais vende
vendas_confirmadas = info_pedidos[info_pedidos['Purchase_Status'] == 'Confirmado'].copy()
vendas_confirmadas['Order_Date'] = pd.to_datetime(vendas_confirmadas['Order_Date'])

#Criando uma tabela para mes e dia
vendas_confirmadas['Dia_Semana'] = vendas_confirmadas['Order_Date'].dt.day_name()
vendas_confirmadas['Mes'] = vendas_confirmadas['Order_Date'].dt.month_name()

#variavel para analisar o quanto os clientes gasta por media em cada compra
ticket_medio = Faturamento / len(vendas_confirmadas)

#Variavel para analisar os top 5 produtos que mais gera faturamento
carrinho_detalhado = pd.merge(carrinho, produtos_vendidos, left_on='Product', right_on='Product_Name')
carrinho_detalhado['Faturamento_Item'] = carrinho_detalhado['Quantity'] * carrinho_detalhado['Price_y']
faturamento_por_produto = carrinho_detalhado.groupby('Product_Name')['Faturamento_Item'].sum()

print(f"Limite superior: R$ {limite_superior:.2f}")
print(f"Quantidade de pedidos comuns: {len(pedidos_normais)}")
print(f"Quantidade de pedidos Vip: {len(pedidos_vip)}")
print(f"Faturamento Total Confirmado: {Faturamento}")
print(f"Produtos mais vendidos: \n{carrinho['Product'].value_counts().head()}")
print(f"Dias que mais vende: \n{vendas_confirmadas['Dia_Semana'].value_counts()}")
print(f"Mês que mais vende: \n{vendas_confirmadas['Mes'].value_counts()}")
print(f"Ticket Médio das vendas confirmadas: R$ {ticket_medio:.2f}")
print(f"Top 5 produtos que mais geram faturamento:\n{faturamento_por_produto.sort_values().head()}")