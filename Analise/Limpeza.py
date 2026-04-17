import pandas as pd

produtos = pd.read_csv(r"C:\Users\andre\OneDrive\Documents\Repositorios\aprendizagem\EBAC\python\Projetos\E-commerce\Dados\DIM_Products.csv")
info_pedidos = pd.read_csv(r"C:\Users\andre\OneDrive\Documents\Repositorios\aprendizagem\EBAC\python\Projetos\E-commerce\Dados\FACT_Orders.csv")
produtos_vendidos = pd.read_csv(r"C:\Users\andre\OneDrive\Documents\Repositorios\aprendizagem\EBAC\python\Projetos\E-commerce\Dados\DIM_Products.csv")
info_clientes = pd.read_csv(r"C:\Users\andre\OneDrive\Documents\Repositorios\aprendizagem\EBAC\python\Projetos\E-commerce\Dados\DIM_Customer.csv")
info_entrega = pd.read_csv(r"C:\Users\andre\OneDrive\Documents\Repositorios\aprendizagem\EBAC\python\Projetos\E-commerce\Dados\DIM_Delivery.csv")


print(info_clientes.isnull())