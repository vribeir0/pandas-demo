import pandas as pd
#Opção para que todas as linhas sejam exibidas no print
pd.set_option('display.max_rows', None)

df_companies = pd.read_csv("DadosEmpresa.csv")
df_address = pd.read_csv("DadosEndereco.csv")

print("Nome das colunas")
for column in df_companies.columns : print(column)

print("Primeiras linhas do arquivo")
print(df_companies.head())
print("Quantidade de empresas que optam pelo simples nacional:\n", df_companies[df_companies['opcao_pelo_simples'] == 'SIM'].shape[0])
print("Soma do capital social:", df_companies['capital_social'].sum())
print("Empresas com capital social entre 10000 e 20000:\n", df_companies.query("capital_social > 10000 and capital_social < 20000"))

df_curitiba_companies = df_companies.merge(df_address, left_on='cnpj', right_on='cnpj').query("municipio == 'CURITIBA'")
df_curitiba_companies.to_csv("DadosEmpresaCuritiba.csv", index=False)
