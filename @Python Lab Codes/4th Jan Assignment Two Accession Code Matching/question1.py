import pandas as pd

file1_path = "filtered_Homo_sapience.csv"

df1 = pd.read_csv(file1_path)

#Path to e_file2.csv
file2_path = "e_file.csv"
# Read the e_file2.csv with headers
df2 = pd.read_csv(file2_path, header=None, names=["Accession Code(1)", "Accession Code(2)"])

# Create an empty DataFrame 
matching_pairs = pd.DataFrame(columns=["Accession Code(1)", "Accession Code(2)"])

#To find matching rows in df2
for _, row in df1.iterrows():
    # Splitting the Accession Code(s) into a set
    accessions = set(row["Accession Code(s)"].split(','))
    
    # Filtering rows in df2 
    matching_rows = df2[df2.isin(accessions).any(axis=1)]
    
    #if matching rows are found, append them to matching_pairs
    if not matching_rows.empty:
        matching_pairs = pd.concat([matching_pairs, matching_rows])

matching_pairs = matching_pairs.drop_duplicates()

# Saving the matching pairs into a CSV file
matching_pairs.to_csv("All_Matched_pairs.csv", index=False)