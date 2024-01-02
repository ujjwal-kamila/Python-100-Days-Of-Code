##2. From the above-generated file, against each pdb id generate accession codes combinations of two and store them for each pdb id. 
# for example: pdb id say, ix2b and access codes are a, b, c. Then store then this way,
# ix2b: [[a,b],[b,c],[c,a]]

# 2nd Part 
import pandas as pd

data = pd.read_csv("New_Output_file.csv")

df = pd.DataFrame(data)

# Dictionary to hold combinations for each Entry ID
pdb_combinations = {}

# Iterating through each row in the DataFrame
for index, rows in df.iterrows():
    # Splitting the 'Accession Code(s)' string into a list
    accession_codes = str(rows['Accession Code(s)']).split(',')
    combinations = []

    # Generating combinations 
    for i in range(len(accession_codes)):
        for j in range(i + 1, len(accession_codes)):
            combinations.append([accession_codes[i], accession_codes[j]])
        
    # Storing combinations for the current Entry ID in the dictionary
    pdb_combinations[rows['Entry ID']] = combinations

# Printing combinations for each Entry ID
for entry_id, combinations in pdb_combinations.items():
    print(f"{entry_id}: {combinations}")

# Writing combinations store into a text file named "Final_combinations.txt"
file_name = 'Final_combinations.txt'
with open(file_name, 'w') as file:
    for pdb_id, combinations_list in pdb_combinations.items():
        file.write(f"{pdb_id}: {combinations_list}\n")
