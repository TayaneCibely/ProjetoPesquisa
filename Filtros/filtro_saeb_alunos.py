import pandas as pd 

# Carregar o arquivo csv com codificação 'ISO-8859-1', possível usar utf-8
df = pd.read_csv('TS_ALUNO_3EM_ESC.csv', sep=',', encoding='ISO-8859-1')

# Filtrar os dados de Pernambuco (PE)
df_pernambuco = df[df['ID_UF']==26]

# Filtrar os dados da Paraíba (PB)
df_paraiba = df[df['ID_UF']==25]

# Salvar os dados filtrados em arquivos CSV separados
df_pernambuco.to_csv('dados_pernambuco_saeb_alunos.csv', index=False, sep=';')
df_paraiba.to_csv('dados_paraiba_saeb_alunos.csv', index=False, sep=';')