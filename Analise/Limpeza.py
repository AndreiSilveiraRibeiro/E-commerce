import pandas as pd
import numpy as np

info_pedidos = pd.read_csv(r".\Dados\FACT_Orders.csv")
produtos_vendidos = pd.read_csv(r".\Dados\DIM_Products.csv")
info_clientes = pd.read_csv(r".\Dados\DIM_Customer.csv")
info_entrega = pd.read_csv(r".\Dados\DIM_Delivery.csv")

tabelas = {
    "Pedidos": info_pedidos,
    "Clientes": info_clientes,
    "Entregas": info_entrega,
    "Produtos Vendidos": produtos_vendidos
}

for nome, df in tabelas.items():
    print(f"\n" + "="*30)
    print(f" ANALISANDO TABELA: {nome.upper()} ")
    print("="*30)
    
    # 1. Duplicados e Nulos (Informações quantitativas)
    print(f"✓ Registros Duplicados: {df.duplicated().sum()}")
    print(f"\n✓ Quantidade de Nulos por Coluna:")
    print(df.isnull().sum())
    
    # 2. Tipos e Memória (Informação estrutural)
    print(f"\n✓ Estrutura e Tipagem:")
    df.info() # Ele já imprime sozinho com os detalhes que você precisa