import pandas as pd

dataFile = pd.read_csv("figuras.csv")

areas = []
perimetros = []

for index, row in data.File.iterrows():
        print(f"Fila {index}: FIGURA={row['FIGURA']}, Medida1={row['MEDIDA1']}, MEDIDA2={row['MEDIDA2']}")
