import pandas as pd
import numpy as np

info_pedidos = pd.read_csv(r"C:\Users\andre\OneDrive\Documents\Repositorios\aprendizagem\EBAC\python\Projetos\E-commerce\Dados\FACT_Orders.csv")
produtos_vendidos = pd.read_csv(r"C:\Users\andre\OneDrive\Documents\Repositorios\aprendizagem\EBAC\python\Projetos\E-commerce\Dados\DIM_Products.csv")
info_clientes = pd.read_csv(r"C:\Users\andre\OneDrive\Documents\Repositorios\aprendizagem\EBAC\python\Projetos\E-commerce\Dados\DIM_Customer.csv")
info_entrega = pd.read_csv(r"C:\Users\andre\OneDrive\Documents\Repositorios\aprendizagem\EBAC\python\Projetos\E-commerce\Dados\DIM_Delivery.csv")

print(info_pedidos.head())

#Analisar primeiro as informações dos pedidos para ver se tem outliers
print(info_pedidos.describe().loc[['mean', '25%', '50%', '75%', 'max']])

Q1 = info_pedidos['Total'].quantile(0.25)
Q3 = info_pedidos['Total'].quantile(0.75)
IQR = Q3 - Q1

limite_superior = Q3 + (1.5 * Q1)

pedidos_normais = info_pedidos[info_pedidos['Total'] <= limite_superior]

pedidos_vip = info_pedidos[info_pedidos['Total'] > limite_superior]


print(f"Limite superior: R$ {limite_superior:.2f}")
print(f"Quantidade de pedidos comuns: {len(pedidos_normais)}")
print(f"Quantidade de pedidos comuns: {len(pedidos_vip)}")