import pandas as pd

inicio = int(input('Qual a primeira referência? '))
fim = int(input('Qual a última referencia? '))

produto1 = pd.read_excel("C:/Users/Leandro/PyCharm/Python/Relatório de Estoque/PRODUTO1.xlsx", sep=';')
produto2 = pd.read_excel("C:/Users/Leandro/PyCharm/Python/Relatório de Estoque/PRODUTO2.xlsx", sep=';')
produto3 = pd.read_excel("C:/Users/Leandro/PyCharm/Python/Relatório de Estoque/PRODUTO3.xlsx", sep=';')
produto4 = pd.read_excel("C:/Users/Leandro/PyCharm/Python/Relatório de Estoque/PRODUTO4.xlsx", sep=';')

produto1 = pd.DataFrame(produto1[['COD_EST', 'DESCRICAO', 'VALOR_VEND', 'ULT_CUSTO', 'SALDO_ATU']].rename(columns={'COD_EST': 'Codigo', 'DESCRICAO': 'Descrição', 'VALOR_VEND': 'Venda', 'ULT_CUSTO': 'Custo', 'SALDO_ATU': 'L4'}))
produto1 = produto1.sort_values(by='Codigo', ignore_index=True)
produto1['Venda'] = produto1['Venda'].round(2)
produto1['Custo'] = produto1['Custo'].round(0)

produto2 = pd.DataFrame(produto2[['COD_EST', 'DESCRICAO', 'VALOR_VEND', 'ULT_CUSTO', 'SALDO_ATU']].rename(columns={'COD_EST': 'Codigo', 'DESCRICAO': 'Descrição', 'VALOR_VEND': 'Venda', 'ULT_CUSTO': 'Custo'}))
produto2 = produto2.sort_values(by='Codigo', ignore_index=True)

produto3 = pd.DataFrame(produto3[['COD_EST', 'DESCRICAO', 'VALOR_VEND', 'ULT_CUSTO', 'SALDO_ATU']].rename(columns={'COD_EST': 'Codigo', 'DESCRICAO': 'Descrição', 'VALOR_VEND': 'Venda', 'ULT_CUSTO': 'Custo'}))
produto3 = produto3.sort_values(by='Codigo', ignore_index=True)

produto4 = pd.DataFrame(produto4[['COD_EST', 'DESCRICAO', 'VALOR_VEND', 'ULT_CUSTO', 'SALDO_ATU']].rename(columns={'COD_EST': 'Codigo', 'DESCRICAO': 'Descrição', 'VALOR_VEND': 'Venda', 'ULT_CUSTO': 'Custo'}))
produto4 = produto4.sort_values(by='Codigo', ignore_index=True)

dados = produto1
dados['L2'] = produto2['SALDO_ATU']
dados['RT'] = produto4['SALDO_ATU']
dados['EST'] = produto3['SALDO_ATU']
dados['Total'] = dados['L4'] + dados['L2'] + dados['EST'] + dados['RT']

dados['Codigo'] = pd.to_numeric(dados['Codigo'], errors='coerce')
selecao = (dados['Codigo'] >= inicio) & (dados['Codigo'] <= fim)
dados_selecao = dados[selecao]
dffinal = dados_selecao

dffinal.to_excel('Relatório_Estoque.xlsx', index=False)

