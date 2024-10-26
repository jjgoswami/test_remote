# Open the file in read mode
file_content = open('data_content.txt', 'r')

# Read all lines from the file
line_content = file_content.readlines()

# Print each line
for line in line_content:
    if "capital" in line:
        print(f" The content with capital word is here : {line.strip()}")
    # .strip() removes any trailing newline or spaces

# Close the file after reading
file_content.close()
