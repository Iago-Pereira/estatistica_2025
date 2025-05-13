# %%

import pandas as pd
# %%

df = pd.read_csv("data/points_tmw.csv")
df.head()
# %%

print("Estatísticas de Posição para Transações:")

minimo = df["qtdPontos"].min()
print(f"Mínimo: {minimo}")

media = df["qtdPontos"].mean()
print(f"Média: {media}")

quartil_1 = df["qtdPontos"].quantile(0.25)
print(f"1º Quartil: {quartil_1}")

mediana = df["qtdPontos"].median()
print(f"Mediana: {mediana}")

quartil_3 = df["qtdPontos"].quantile(0.75)
print(f"3º Quartil: {quartil_3}")

maximo = df["qtdPontos"].max()
print(f"Máximo: {maximo}")

variancia = df["qtdPontos"].var()
print(f"Variância: {variancia}")

desvio_padrão = df["qtdPontos"].std()
print(f"Desvio Padrão: {desvio_padrão}")

amplitude = df["qtdPontos"].max() - df["qtdPontos"].min()
print(f"Amplitude: {amplitude}")
# %%

df["qtdPontos"].describe()
# %%

usuarios = (df.groupby(["idUsuario"])
              .agg({
                  "idTransacao": "count",
                  "qtdPontos": "sum",
            }).reset_index())

usuarios
# %%

usuarios[["idTransacao", "qtdPontos"]].describe()