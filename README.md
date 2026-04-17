# 📊 Análise de Dados - E-commerce

Este projeto faz parte da minha formação em **Análise de Dados na EBAC**. O objetivo foi analisar o comportamento de vendas de um e-commerce, identificar padrões sazonais e entender a performance dos produtos.

## 🛠️ Tecnologias Utilizadas
* **Python** (Lógica principal)
* **Pandas** (Tratamento e limpeza de dados)
* **Matplotlib / Seaborn** (Visualização de dados)

## 📈 Insights Extraídos
Aqui estão os principais pontos descobertos durante a análise:

1. **Sazonalidade:** O mês de **Março** apresentou o maior volume de vendas.
2. **Ticket Médio:** O valor médio gasto por compra confirmada foi de **R$ 2470.23**.
3. **Top Produtos de Faturamento:** O item **ACER Notebook Gamer Nitro** é o líder em faturamento.
4. **Top Produtos mais Vendidos:** O item **Fone de ouvido Sem Fio QCY T27** é o líder em vendas.
5. **Outliers:** Identifiquei pedidos "VIP" (acima de **R$ 8,320.23**) que representam uma **oportunidade** de marketing personalizado.
6. **Estratégia Comercial**: Identificamos um pico de volume aos **Domingos e Segundas**. Isso sugere uma **oportunidade** para antecipar campanhas de marketing nas sextas-feiras e sábados, visando **capturar essa demanda** reprimida do início da semana.

## 🚀 Como Rodar o Projeto
1. Clone o repositório.
2. Certifique-se de ter os arquivos CSV na pasta `.\Dados\`.
3. Execute o arquivo `analise.py`.

## 🧠 Desafios Técnicos
Durante o projeto, implementei:
* **Cálculo de IQR** para identificação estatística de outliers.
* **Caminhos Relativos** para garantir que o código rode em qualquer máquina.
* **Tratamento de Datas** para ordenação cronológica correta nos gráficos.