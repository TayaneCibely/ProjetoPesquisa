import pandas as pd 

# Carregar o arquivo csv com codificação 'ISO-8859-1', possível usar utf-8
df = pd.read_csv('microdados_ed_basica_2017.csv', sep=';', encoding='ISO-8859-1')

# Filtrar os dados de Pernambuco (PE)
df_pernambuco = df[df['SG_UF']=='PE']

# Filtrar os dados da Paraíba (PB)
df_paraiba = df[df['SG_UF']=='PB']

# Salvar os dados filtrados em arquivos CSV separados
df_pernambuco.to_csv('dados_pernambuco_censo.csv', index=False, sep=';')
df_paraiba.to_csv('dados_paraiba_censo.csv', index=False, sep=';')
