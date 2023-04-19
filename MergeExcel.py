import os
import pandas as pd
path = "C:/Users/bbattaglia/ICONSULTING S.p.A/Moncler - Documents/Progetti/MONCDC - payment control - 23/Sviluppo/Claims/2022"
files = os.listdir(path) 

## Method 1 gets the first sheet of a given file


df = pd.DataFrame()
dfs = [] # lista vuota per contenere i dataframe
for file in files:
    if file.endswith('.xlsx'):
        data = pd.read_excel(path+'/'+file)
        data = data.assign(file_name=file) # aggiungi colonna file_name
        dfs.append(data) # aggiungi il dataframe alla lista
    df = pd.concat(dfs, sort=False) # unisci tutti i dataframe
df.head() # stampa i primi 5 record


df.to_excel(path+'/claims.xlsx')