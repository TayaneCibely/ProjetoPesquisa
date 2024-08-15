import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('microdados_ed_basica_2017.csv', sep=';', encoding='ISO-8859-1')

# Filtrar apenas as linhas onde a região é "Nordeste"
df_nordeste = df[df['NO_REGIAO'] == 'Nordeste']

# Salvar o novo dataframe em um arquivo CSV
df_nordeste.to_csv('dados_nordeste.csv', index=False, sep=';')
