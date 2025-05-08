# %%

import pandas as pd
import sqlalchemy

# %%

df = pd.read_csv("data/points_tmw.csv")
df.head()

# %%

# Criando tabela do DB
engine = sqlalchemy.create_engine("sqlite:///data/tmw.db")

df.to_sql("points", engine, if_exists="replace", index=False)
# %%

pd.value_counts(df["descProduto"])
# %%

# Evitando a depreciação
df["descProduto"].value_counts()
# %%

# Mesmo proposito com group by transformando em df
freq_produto = df.groupby(["descProduto"])[["idTransacao"]].count()

freq_produto["Freq. Abs. Acum."] = freq_produto["idTransacao"].cumsum()

freq_produto["Freq. Rel."] = freq_produto["idTransacao"] / freq_produto["idTransacao"].sum()

freq_produto["Freq. Rel. Acum."] = freq_produto["Freq. Rel."].cumsum() 

freq_produto = freq_produto.rename(columns={"idTransacao": "Freq. Abs."})
freq_produto
# %%

freq_catProduto = df.groupby(["descCategoriaProduto"])[["idTransacao"]].count()

freq_catProduto["Freq. Abs. Acum."] = freq_catProduto["idTransacao"].cumsum()

freq_catProduto["Freq. Rel."] = freq_catProduto["idTransacao"] / freq_catProduto["idTransacao"].sum()

freq_catProduto["Freq. Rel. Acum."] = freq_catProduto["Freq. Rel."].cumsum()

freq_catProduto = freq_catProduto.rename(columns={"idTransacao": "Freq. Abs."})
freq_catProduto
# %%
