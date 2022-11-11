import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("casasboston.csv")
df = datos.rename(columns={
    "TOWN": "CIUDAD",
    "CRIM": "INDICE_CRIMEN",
    "INDUS": "PCT_ZONA_INDUSTRIAL",
    "CHAS": "RIO_CHARLES",
    "RM": "N_HABITACIONES_MEDIO",
    "MEDV": "VALOR_MEDIANO",
    "LSTAT": "PCT_CLASE_BAJA"
})

print(df.sample(5))
df.N_HABITACIONES_MEDIO.plot.hist()
plt.show()

df.INDICE_CRIMEN.plot.hist(bins=100, xlim=(0,20))
plt.show()

df.plot.scatter(x="INDICE_CRIMEN", y="VALOR_MEDIANO", alpha=0.2)
plt.show()

valor_por_ciudad = df.groupby("CIUDAD")["VALOR_MEDIANO"].mean()
valor_por_ciudad.head(10).plot.barh()
plt.show()

df["VALOR_CUANTILES"] = pd.qcut(df.VALOR_MEDIANO, 5)
df.boxplot(column="INDICE_CRIMEN", by="VALOR_CUANTILES",figsize=(8,6))
plt.show()