# 1. From the Homo sapience file already shared with you, obtain all the pdb ids with only three accession codes of organism Homo sapience. Write those pdb ids with organism and accession codes in a separate csv file. 


import pandas as pd
# Read the CSV file
data_frame = pd.read_csv('homo_sapiens.csv')

# Custom function to fill empty blocks in a column 
def custom_ffill(column):
    non_empty_value = None
    result = []
    for value in column:
        if pd.notnull(value):
            non_empty_value = value
        result.append(non_empty_value)
    return pd.Series(result)

#Function to drop rows with empty values in a specified column
def custom_dropna(data_frame, column):
    return data_frame[data_frame[column].notnull()]

#Function to split rows with multiple values in a column
def custom_split(column):
    return column.str.split(',')

#Function to explode rows for each value in a column
def custom_explode(data_frame, column):
    new_rows = []
    for index, row in data_frame.iterrows():
        values = row[column]
        for value in values:
            new_row = row.copy()
            new_row[column] = value
            new_rows.append(new_row)
    return pd.DataFrame(new_rows)

#function to filter rows based on a condition in a specified column
def custom_filter(data_frame, column, condition):
    return data_frame[data_frame[column] == condition]

# function to group by a column and aggregate other columns
def custom_group_and_aggregate(data_frame, group_column, aggregation_dict):
    return data_frame.groupby(group_column, sort=False).agg(aggregation_dict)

# Custom function to filter rows based on a condition applied to a column
def custom_filter_condition(data_frame, column, condition_function):
    return data_frame[condition_function(data_frame[column])]

# Custom function to print the new dataframe
def custom_print(data_frame):
    print(data_frame.head())

# Custom function to save the result to a new CSV file
def custom_to_csv(data_frame, output_file):
    data_frame.to_csv(output_file, index=True)

# Fill empty blocks in 'Entry ID' column with the previous non-empty value
data_frame["Entry ID"] = custom_ffill(data_frame["Entry ID"])

# Drop rows with empty values in the third column
data_frame = custom_dropna(data_frame, 'Accession Code(s)')

# Split rows with multiple Accession Code(s)
data_frame['Accession Code(s)'] = custom_split(data_frame['Accession Code(s)'])

#Creating new rows for each Accession Code
data_frame = custom_explode(data_frame, 'Accession Code(s)')

# Filter rows with 'Source Organism' as "Homo sapiens"
data_frame_homo_sapiens = custom_filter(data_frame, 'Source Organism', 'Homo sapiens')

# Group by entry id and aggregate the other columns
data_frame_new = custom_group_and_aggregate(data_frame_homo_sapiens, "Entry ID", {
    "Source Organism": "first",
    "Accession Code(s)": lambda x: ','.join(x)
})

# Filter rows where Accession Code(s) has a list length of 3
data_frame_new2 = custom_filter_condition(data_frame_new, 'Accession Code(s)', lambda x: x.str.count(',') == 2)

# Print the new dataframe
custom_print(data_frame_new2)

# Save the result to a new CSV file "New_Output_file.csv"
custom_to_csv(data_frame_new2, 'New_Output_file.csv')
