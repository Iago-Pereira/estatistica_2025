# %%

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%

df = pd.read_csv("data/points_tmw.csv")
df.head()
# %%

group_prod = (df.groupby("descProduto")["idTransacao"]
                .count()
                .reset_index())

group_prod = group_prod.sort_values(by="idTransacao")
# %%

sns.set_theme(style="whitegrid")
plt.figure(figsize=(6,4))
sns.barplot(group_prod, y="descProduto", x="idTransacao")
plt.xlabel("Quantidade Transacoes")
plt.ylabel("Produto")
plt.title("Frequencia de Produtos")
plt.show()
# %%

df["dataTransacao"] = pd.to_datetime(df["dtTransacao"]).dt.date
group_data = df.groupby("dataTransacao").agg(
    {"qtdPontos": "sum",
     "idTransacao": "count",}
).reset_index()

group_data - group_data.sort_values(by="dataTransacao")
group_data
# %%

plt.figure(figsize=(8,6))
plt.plot(group_data["dataTransacao"], group_data["idTransacao"])
plt.ylabel("Qtde Transações")
plt.title("Série Histórica de Transações")
plt.legend(["Qtde Transações"])
# %%

plt.hist(group_data["qtdPontos"], bins=30)
plt.xlabel("Pontos")
plt.ylabel("Frequência")
plt.show()
# %%

plt.figure(figsize=(8, 8))
plt.boxplot(group_data["qtdPontos"])
plt.title("Box-Plot")
plt.ylabel("Pontos")
# %%

# Melhor representado por gráfico de barras, pois boxplot demonstra muitos outliers
group_pontos = (df.groupby("qtdPontos")["idTransacao"]
                  .count()
                  .reset_index())

sns.barplot(group_pontos, x="qtdPontos", y="idTransacao")
plt.show()
# %%

sns.scatterplot(group_data, x="qtdPontos", y="idTransacao")
# %%
