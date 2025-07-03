import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# t = np.linspace(0, 2*np.pi,100)
# y = np.cos(3*t)

# plt.plot(t,y)
# plt.show()

# url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSLFUQs9xRNETTfeVjcQgWMo_eY-qZAmyv7VJUscmnN6osUHmdN48KdQWTmN8Ea_-KDZe5W4Y2W2fQ8/pub?output=csv'
# df = pd.read_csv(url)

# print(df)

produtos = ["poço", "painel", "bomba", "Regulamentação", "agua", "limpeza"]
precos = [15000, 550, 1100, 400, 100, 150]
unidades = [12, 12, 16, 6, 10, 10]
vendas = [6,6,8, 1, 3, 1]
faturamento_total = 0
faturamento = []
for i in range(len(precos)):
  faturamento.append(precos[i]*vendas[i])
  faturamento_total += precos[i]*vendas[i]
faturamento_total
print(precos)
print(produtos)
print(unidades)
print(faturamento)
print(vendas)
print(faturamento_total )

# calcular faturamento


print("Faturamento total no mês: ",faturamento_total )

df = pd.DataFrame(zip(produtos,precos,unidades,vendas,faturamento),
             columns=['Nome produto','precos','quantidade','Vendas','valor total'])

print(df)

#filtragem por quantidade de itens de acordo com a coluna
colunaFiltro = "Vendas"

# for coluna in colunaFiltro:
#   query += (f'`{coluna}`')
# query +=  ("Vendas")

maiorVenda = df.query(f'`{colunaFiltro}` == `{colunaFiltro}`.max()')
print(maiorVenda)

# produto mais vendido:
maiorVenda = df.query(f'`{colunaFiltro}` == `{colunaFiltro}`.max()')
print(maiorVenda)

# # produto menos vendido:
menorVenda = df.query(f'`{colunaFiltro}` == `{colunaFiltro}`.min()')
print(menorVenda)


# # vendas em order decrecente:
vendasDecrescente = df.sort_values(colunaFiltro, ascending=False)
print(vendasDecrescente)

# # vendas em order crecente:
vendasCrecente = df.sort_values(colunaFiltro, ascending=True)
print(vendasCrecente)



# Use the 'Nome produto' column for x-axis and 'Vendas' for y-axis from the dataframe
x = df['Nome produto']
y = df['Vendas']

plt.figure(figsize=(10, 5)) # Adjust figure size for better readability
plt.bar(x, y, color = "#4CAF50")
plt.xlabel("Produto") # Add x-axis label
plt.ylabel("Vendas") # Add y-axis label
plt.title("Vendas por Produto") # Add title
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.tight_layout() # Adjust layout to prevent labels overlapping
plt.show()