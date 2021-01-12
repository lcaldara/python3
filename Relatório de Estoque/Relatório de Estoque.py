import pandas as pd
import shutil
import os
import glob

path = 'C:/Users/Leo/Python/Relatório de Estoque/dados/'
save_path = 'C:/Users/Leo/Python/Relatório de Estoque/'
files = glob.glob(os.path.join(path, '*'))


def welcome_msg():
    print('******************************************************************')
    print('**************                                     ***************')
    print('**************        RELATÓRIO DE ESTOQUE         ***************')
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

delete_files = str(input(f'Deseja deletar os arquivos antigos [S/N]? ')).upper()[0]

while delete_files not in 'SN':
    delete_files = str(input('Escolha [S/N]: ')).upper()[0]

if delete_files == 'S':
    clear_folder()
    getting_files()
    print(f'\n******************************************************************')

    x = str(input('\nSalve os arquivos como .xlsx e aperte "C" para continuar: ')).upper()[0]

    while x not in 'C':
        x = str(input('Aperte "C" para continuar: ')).upper()[0]

print(f'\n******************************************************************\n')

inicio = int(input('Qual a primeira referência? '))
fim = int(input('Qual a última referencia? '))

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

dados['Codigo'] = pd.to_numeric(dados['Codigo'], errors='coerce')
selecao = (dados['Codigo'] >= inicio) & (dados['Codigo'] <= fim)
dados_selecao = dados[selecao]
dffinal = dados_selecao

dffinal.to_excel(f'Relatório_Estoque_{inicio}-{fim}.xlsx', index=False)

print(f'\n******************************************************************\n')

print(f'O arquivo foi salvo em {save_path}')

print(f'\n******************************************************************')

input(f'\nAperte qualquer tecla para encerrar... ')
