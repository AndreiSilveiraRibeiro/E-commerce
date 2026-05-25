import pandas as pd

print("==================================================")
print("   CRUZAMENTO FINAL DE DADOS PARA O LOOKER STUDIO")
print("==================================================")

# 1. Carregar as bases apontando para a pasta Dados
info_pedidos = pd.read_csv("./Dados/FACT_Orders.csv")
info_clientes = pd.read_csv("./Dados/DIM_Customer.csv")
info_entrega = pd.read_csv("./Dados/DIM_Delivery.csv")

# 2. Filtrar apenas as vendas confirmadas
vendas_confirmadas = info_pedidos[info_pedidos['Purchase_Status'] == 'Confirmado'].copy()
vendas_confirmadas['Order_Date'] = pd.to_datetime(vendas_confirmadas['Order_Date'])

# Criar colunas de data em português para facilitar no Looker Studio
traducao = {
    'January': 'Janeiro', 'February': 'Fevereiro', 'March': 'Março',
    'April': 'Abril', 'May': 'Maio', 'June': 'Junho',
    'July': 'Julho', 'August': 'Agosto', 'September': 'Setembro',
    'October': 'Outubro', 'November': 'Novembro', 'December': 'Dezembro'
}
vendas_confirmadas['Mes'] = vendas_confirmadas['Order_Date'].dt.month_name().map(traducao)

# 3. Fazer o Cruzamento (Merge) usando a chave 'Id'
print("[INFO] Unificando tabelas de Pedidos, Clientes e Logística...")
df_consolidado = pd.merge(vendas_confirmadas, info_clientes, on="Id", how="inner")
df_consolidado = pd.merge(df_consolidado, info_entrega, on="Id", how="inner")

# 4. Salvar o arquivo final NA RAIZ DO PROJETO com encoding UTF-8 com BOM
# Salvando na raiz evita erros de caminhos perdidos
df_consolidado.to_csv(r".\Dados\base_consolidada_ecommerce_final.csv", index=False, encoding='utf-8-sig')

print("\n🚀 Sucesso! O arquivo 'base_consolidada_ecommerce_final.csv' foi gerado na raiz.")
print(f"Total de linhas geradas: {len(df_consolidado)}")