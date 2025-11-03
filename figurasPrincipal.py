import pandas as pd
from funciones import a_triangulo, p_triangulo, a_rectangulo, p_rectangulo, a_circulo, p_circulo 


dataFile = pd.read_csv("figuras.csv")

print("Procesando figuras ...\n")

areas = []
perimetros = []

for index, row in dataFile.iterrows():
   if row['FIGURA'] == 't':
      area = a_triangulo(int(row['MEDIDA1']), int(row['MEDIDA2']))
      perimetro = p_triangulo(int(row['MEDIDA1']))
   elif row["FIGURA"] == 'r':
      area = a_rectangulo(int(row["MEDIDA1']), int(row['MEDIDA2']))
      perimetro = p_rectangulo(int(row['MEDIDA1']), int(row['MEDIDA2]))
   elif row ['FIGURA'] == 'c':
      area = round(a_circulo(float(row['MEDIDA1'])),2)
      perimetro = round(p_circulo(float(row['MEDIDA1'])),2)
print(f"Fila{index}: FIGURA={row['FIGURA']}, Medida1={row['MEDIDA1]}, Medida2={row['MEDIDA2']}, Area={area}, Perímetro={perimetro}")
