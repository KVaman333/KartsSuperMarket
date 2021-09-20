import pandas as pd




read_file = pd.read_excel(r'Karts-Inventory.xlsx')
read_file.to_csv(r'Karts-Inventory.csv',index=None,header=True)