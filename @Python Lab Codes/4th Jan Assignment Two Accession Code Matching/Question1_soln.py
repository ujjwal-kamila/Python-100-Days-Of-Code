import pandas as pd

# Read the first file
file1_path = "filtered_Homo_sapience.csv"
df1 = pd.read_csv(file1_path)

# Read the second file with specific headers
file2_path = "e_file.csv"
df2 = pd.read_csv(file2_path, header=None, names=["Accession1", "Accession2"])

# Function to check if any accession code is present in a row of df2
def check_accession(row):
    accessions = set(row["Accession Code(s)"].split(','))
    return df2[df2.isin(accessions).any(axis=1)]

# Apply the function to each row in df1 and concatenate the matches
matching_pairs = pd.concat([check_accession(row) for _, row in df1.iterrows()])

# Drop duplicates from the matching pairs
matching_pairs = matching_pairs.drop_duplicates()

# Save the matching pairs to a CSV file
matching_pairs.to_csv("Matched_Pairs.csv", index=False)
