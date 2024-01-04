#part 1
import pandas as pd
from itertools import combinations
df = pd.read_csv('Homo_sapiens.csv')
df['Entry ID'] = df['Entry ID'].fillna(method='ffill')
df['Accession Code(s)'] = df['Accession Code(s)'].apply(lambda x: str(x).split(',') if pd.notna(x) else [])
exploded_df = df.explode('Accession Code(s)')
filtered_df = exploded_df[exploded_df['Source Organism'] == 'Homo sapiens'].groupby(['Entry ID', 'Source Organism']).filter(lambda x: x['Accession Code(s)'].count() == 3)
result_df = filtered_df.groupby(['Entry ID', 'Source Organism'])['Accession Code(s)'].apply(lambda x: ','.join(str(code) for code in x.dropna())).reset_index()
result_df.to_csv('filtered_Homo_sapience.csv', index=False)
df = pd.read_csv('filtered_Homo_sapience.csv')
combinations_dict = {}
for index, row in df.iterrows():
    entry_id = row['Entry ID']
    accession_codes = row['Accession Code(s)'].split(',')
    code_combinations = list(combinations(accession_codes, 2))
    combinations_dict.setdefault(entry_id, []).extend(code_combinations)
result_df = pd.DataFrame(list(combinations_dict.items()), columns=['Entry ID', 'Accession Code Combinations'])
result_df.to_csv('accession_code_combinations.csv', index=False)