import ast
import csv

# Path to the file containing the array
file_path = r"./array.json"

# Function to read and parse the array from the file
def read_array_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read the file content
        file_content = file.read()
        # Safely evaluate the string as a Python expression
        array = ast.literal_eval(file_content)
    return array

# Use the function to read the array
array = read_array_from_file(file_path)

adjusted_array = [[x, y, z-40, r, g, b] for x, y, z, r, g, b in array]



# File path for the CSV
file_path = r'adjusted_array.json'

with open(file_path, 'w') as file:
    file.write(str(adjusted_array))