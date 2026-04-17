import pandas as pd
import numpy as np

info_pedidos = pd.read_csv(r"C:\Users\andre\OneDrive\Documents\Repositorios\aprendizagem\EBAC\python\Projetos\E-commerce\Dados\FACT_Orders.csv")
produtos_vendidos = pd.read_csv(r"C:\Users\andre\OneDrive\Documents\Repositorios\aprendizagem\EBAC\python\Projetos\E-commerce\Dados\DIM_Products.csv")
info_clientes = pd.read_csv(r"C:\Users\andre\OneDrive\Documents\Repositorios\aprendizagem\EBAC\python\Projetos\E-commerce\Dados\DIM_Customer.csv")
info_entrega = pd.read_csv(r"C:\Users\andre\OneDrive\Documents\Repositorios\aprendizagem\EBAC\python\Projetos\E-commerce\Dados\DIM_Delivery.csv")

#Analisando se tem dados nulos e duplicados
print(f'Dados nulos nas informações dos produtos: \n{info_pedidos.isnull().sum()}')
print(f'Dados duplicados nas informações dos produtos: \n{info_pedidos.duplicated().sum()}')

print(f'Dados nulos nas informações dos clientes: \n{info_clientes.isnull().sum()}')
print(f'Dados duplicados nas informações dos clientes: \n{info_clientes.duplicated().sum()}')

print(f'Dados nulos nas informações das entregas: \n{info_entrega.isnull().sum()}')
print(f'Dados nulos nas informações das entregas: \n{info_entrega.duplicated().sum()}')

print(f'Dados nulos nas informações dos produtos vendidos: \n{produtos_vendidos.isnull().sum()}')
print(f'Dados nulos nas informações dos produtos vendidos: \n{produtos_vendidos.duplicated().sum()}')