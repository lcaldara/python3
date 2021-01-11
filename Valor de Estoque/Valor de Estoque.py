import pandas as pd
import shutil
import os
import glob

path = 'C:/Users/Leo/Python/Valor de Estoque/dados/'
files = glob.glob(os.path.join(path, '*'))


def welcome_msg():
    print('******************************************************************')
    print('**************                                     ***************')
    print('**************     CALCULANDO VALOR DE ESTOQUE     ***************')
    print('**************                                     ***************')
    print(f'******************************************************************\n')


def clear_folder():
    if os.path.exists(path):
        for f in files:
            os.remove(f)


def getting_files():
    dbf1 = 'T:/SISTEMAS/SAPE1/PADRAO/PRODUTO.DBF'
    dbf2 = 'T:/SISTEMAS/SAPE2/PADRAO/PRODUTO.DBF'
    dbf3 = 'T:/SISTEMAS/SAPE3/PADRAO/PRODUTO.DBF'
    dbf4 = 'T:/SISTEMAS/SAPE4/PADRAO/PRODUTO.DBF'

    dbfs = [dbf1, dbf2, dbf3, dbf4]

    n = 1
    for d in dbfs:
        shutil.copy(d, os.path.join(path, f'produto{n}.xls'))
        n = n + 1


welcome_msg()
clear_folder()
getting_files()

inicio = int(input('Qual a primeira referência? '))
fim = int(input('Qual a última referencia? '))
print(f'\n******************************************************************')

x = str(input('\nSalve os arquivos como .xlsx e aperte "C" para continuar: ')).upper()[0]

while x not in 'C':
    x = str(input('Aperte "C" para continuar: ')).upper()[0]

print(f'\n******************************************************************')

produto1 = pd.read_excel(os.path.join(path, 'PRODUTO1.xlsx'))
produto2 = pd.read_excel(os.path.join(path, 'PRODUTO2.xlsx'))
produto3 = pd.read_excel(os.path.join(path, 'PRODUTO3.xlsx'))
produto4 = pd.read_excel(os.path.join(path, 'PRODUTO4.xlsx'))

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

dados['Custo L4'] = dados['Custo'] * dados['L4']
dados['Venda L4'] = dados['Venda'] * dados['L4']
dados['Custo L2'] = dados['Custo'] * dados['L2']
dados['Venda L2'] = dados['Venda'] * dados['L2']
dados['Custo RT'] = dados['Custo'] * dados['RT']
dados['Venda RT'] = dados['Venda'] * dados['RT']
dados['Custo EST'] = dados['Custo'] * dados['EST']
dados['Venda EST'] = dados['Venda'] * dados['EST']

dados['Codigo'] = pd.to_numeric(dados['Codigo'], errors='coerce')

selecao = (dados['Codigo'] >= inicio) & (dados['Codigo'] <= fim)
dados_selecao = dados[selecao]
dffinal = dados_selecao

custo_total_4 = sum(dffinal['Custo L4'])
venda_total_4 = sum(dffinal['Venda L4'])
total_pc4 = sum(dffinal['L4'])
custo_total_2 = sum(dffinal['Custo L2'])
venda_total_2 = sum(dffinal['Venda L2'])
total_pc2 = sum(dffinal['L2'])
custo_total_rt = sum(dffinal['Custo RT'])
venda_total_rt = sum(dffinal['Venda RT'])
total_pcRT = sum(dffinal['RT'])
custo_total_3 = sum(dffinal['Custo EST'])
venda_total_3 = sum(dffinal['Venda EST'])
total_pcEST = sum(dffinal['EST'])

print(f'\nCusto Total L4 --> {custo_total_4:.2f}')
print(f'Venda Total L4 --> {venda_total_4:.2f}')
print(f'Peças Total L4 --> {total_pc4:.0f}')
print(f'\nCusto Total L2 --> {custo_total_2:.2f}')
print(f'Venda Total L2 --> {venda_total_2:.2f}')
print(f'Peças Total L2 --> {total_pc2:.0f}')
print(f'\nCusto Total RT --> {custo_total_rt:.2f}')
print(f'Venda Total RT --> {venda_total_rt:.2f}')
print(f'Peças Total RT --> {total_pcRT:.0f}')
print(f'\nCusto Total EST --> {custo_total_3:.2f}')
print(f'Venda Total EST --> {venda_total_3:.2f}')
print(f'Peças Total EST --> {total_pcEST:.0f}')

print(f'\n******************************************************************')
input(f'\nAperte qualquer tecla para encerrar... ')
